import os

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerMessage

from langchain.memory import MongoDBChatMessageHistory
from src.build_LLMChain import build_chain
from src.chain_response import chain_response
from src.history.clear_history import clear_history

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

# build a conversation chain
chain = build_chain(openai_api_key, max_token_limit, temperature)


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
    # message
    msg = event.message.text.strip()
    # message log 
    print(f'{user_id}: has a message')

    # user's message history in MongoDB
    mongodb_message_history = MongoDBChatMessageHistory(
    connection_string=mongo_connection_str, session_id="main", collection_name=user_id
    )
    # request to clear message history
    if (msg == "清除歷史"):
        # clear history
        clear_history(mongodb_message_history)
        reply = "對話歷史已清除"
    # normal message
    else:
        # generate reply
        reply = chain_response(chain, mongodb_message_history, msg)
    # send reply to user
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))

# handle sticker message
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    # user ID
    user_id = event.source.user_id
    # message
    msg = event.message.text.strip()
    # message log 
    print(f'{user_id}: has a message')

    # user's message history in MongoDB
    mongodb_message_history = MongoDBChatMessageHistory(
    connection_string=mongo_connection_str, session_id="main", collection_name=user_id
    )
    # take the second sticker keyword as message
    msg = event.message['keywords'][1]
    
    # generate reply
    reply = chain_response(chain, mongodb_message_history, msg)
    
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