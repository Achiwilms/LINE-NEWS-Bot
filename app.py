import os
import openai
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# LINE keys
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))
# OPENAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Application
app = Flask(__name__)

# response from GPT
def GPT_response(text):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "你是個得力的助手，用中文回答時會用繁體中文"},
            {"role": "user", "content": text},
        ]
    )
    return response["choices"][0]["message"]["content"]


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

# handle message
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # send reply to user
    GPT_answer = GPT_response(event.message.text.strip())
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=GPT_answer))
    
# make url discoverable
@app.route("/", methods=['GET'])
def home():
    return 'Hello World'

# main function
if __name__ == "__main__":
    # port
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)