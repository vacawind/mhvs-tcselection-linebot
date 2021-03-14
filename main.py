

# SDK
# software development kit
# import line official SDK, line聊天機器人開發套件



from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('hblP7CAZGNttUIrBGfRQMeLA4Rp0LVSTtlWQkih5aQTyGUzOVEQtZWtidMPieSAzxcvfA9mqnYi5KaR15qE2cFV7DY+sSgXVZIji1Lml4cwEwOWGKWAK+v27uazwMeXZppE8WMbg9jqAZrOus7NBcwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6f9cd3aceaa33f879598b246548cad91')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你吃飯了嗎?'))


if __name__ == "__main__": # 當user載入SDK時, 有需要才執行, 而不是一載入就執行程式
    app.run()