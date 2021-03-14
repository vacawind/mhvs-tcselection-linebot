

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

line_bot_api = LineBotApi('pRmciVeQZZjKIyuDPdcdBXav7ddMtS+HpQ9QlxlKn8qAb53whkMWPvjqAp6kXRohaTJRYmDnGSfVjH//1iRnMnBUSDP8qgTop1OGrTgTXFJEKjKmkurAwUmsQJHZ9mY6yrl2UDAJsGI3g7ANoytJtAdB04t89/1O/w1cDnyilFU=') # YOUR_CHANNEL_ACCESS_TOKEN
handler = WebhookHandler('0fb25e310330caebb414234d728bcb20') # YOUR_CHANNEL_SECRET' 


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