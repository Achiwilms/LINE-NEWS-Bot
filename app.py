import os, re, openai
from langchain.memory import MongoDBChatMessageHistory
from src.build_ChatChain import build_chat_chain
from src.build_NewsChain import build_news_chain
from src.chain_response import chain_response
from src.history.clear_history import clear_history
from src.news.extract_news import extract_news

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerMessage


# LINE keys
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))
# OpenAI api key
openai_api_key = os.getenv('OPENAI_API_KEY')
# MongoDB connection string
mongo_connection_str = os.getenv('MONGO_CONNECTION_STR')
# max token limit for buffer
max_token_limit = int(os.getenv('MAX_TOKEN_LIMIT'))
# temperature
temperature = float(os.getenv('TEMPERATURE'))

# Application
app = Flask(__name__)

# Define the pattern
url_regex = re.compile(r'https?://\S+')

# build chat chain
chat_chain = build_chat_chain(openai_api_key, max_token_limit, temperature)

# build news chain
news_chain = build_news_chain(openai_api_key, max_token_limit, temperature)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# handle text message
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    # user ID
    user_id = event.source.user_id
    # message log 
    print(f'{user_id}: has a message')
    # message
    msg = event.message.text.strip()

    # user's message history in MongoDB
    mongodb_message_history = MongoDBChatMessageHistory(
    connection_string=mongo_connection_str, session_id="main", collection_name=user_id
    )

    try:
        # request to clear message history
        if (msg == "開啟新對話"):
            # clear history
            clear_history(mongodb_message_history)
            reply = "對話歷史清除完畢，新對話已開始😎"
        # manually input news
        elif (msg.startswith("標題：") or msg.startswith("標題:")):
            # generate chain response
            reply = chain_response(news_chain, mongodb_message_history, msg[3:].strip())
        # conversation
        else:
            # if the string contains a URL
            if url_regex.search(msg):
                # clear history (since it's a new url, very possible a new conversation)
                clear_history(mongodb_message_history)

                # Find the first URL in the message
                url = url_regex.search(msg).group()

                # extract news 
                news = extract_news(url)
                # print(f"{news}")
                
                # push message to tell user the bot is reading
                line_bot_api.push_message(user_id, TextSendMessage(text="收到！正在閱讀報導中..."))

                # generate chain response
                reply = chain_response(news_chain, mongodb_message_history, news)                        
            # normal conversation
            else:
                # generate chain response
                reply = chain_response(chat_chain, mongodb_message_history, msg)

    # openai error
    except openai.error.InvalidRequestError as e:
        error_msg = str(e)
        if (error_msg.startswith("This model's maximum context length is 4097 tokens")):
            reply = '抱歉😅 閱讀過程中發生錯誤，原因可能是:\n1.對話與報導內容過長，請輸入"開啟新對話"後重試\n2.目前還不支援這個網站。你可以將報導連結由此表單:\nhttps://forms.gle/q9XcJyRm9d2d9iBP7 反映給我們，我們會盡速處理並提供支援🔧\n\n此外，你也可以直接輸入報導內容，輸入格式為:\n\n標題：\n[報導標題]\n\n內文：\n[報導內文]'
        else: 
            reply = error_msg
            
    except Exception as e:
        # can't find news error
        error_msg = str(e)
        if error_msg=="找不到報導":
            reply = "抱歉😅 目前還不支援這個網站。\n\n你可以將報導連結由此表單:\nhttps://forms.gle/q9XcJyRm9d2d9iBP7 反映給我們，我們會盡速處理並提供支援🔧\n\n此外，你也可以直接輸入報導內容，輸入格式為:\n\n標題：\n[報導標題]\n\n內文：\n[報導內文]"
        else:
            reply = error_msg

    # send reply to user 
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))

# handle sticker message
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    # user ID
    user_id = event.source.user_id
    # message log 
    print(f'{user_id}: has a message')
    print(event.message['keywords'])
    print(type(event.message['keywords']))

    # sticker has keywords
    if event.message['keywords'] is not None:
        # take the first sticker keyword as message
        msg = "我感到" + ', '.join([keyword for keyword in event.message['keywords']])
        # user's message history in MongoDB
        mongodb_message_history = MongoDBChatMessageHistory(
        connection_string=mongo_connection_str, session_id="main", collection_name=user_id
        )
        # generate reply
        reply = chain_response(chat_chain, mongodb_message_history, msg)
    # sticker doesn't have keywords
    else:
        reply = "抱歉，我看不懂這個貼圖😅 能傳別的貼圖嗎?"
    
    # send reply to user
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))

# make url discoverable
@app.route("/", methods=['GET'])
def home():
    return 'Hello World'

# main function
if __name__ == "__main__":
    # port
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)