from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from comforting_bot_2 import HandleReasons as ComfortBot
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

#接簡易網站
@app.route("/")
def home():
    return render_template("home.html")
#接收line 平台的通知
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    return 'OK'

#學你說話
#@handler.add(MessageEvent, message=TextMessage)
#def echo(event):
#    line_bot_api.reply_message(
        
#        event.reply_token,
#        TextMessage(text=event.message.text)
        
#    )

@handler.add(MessageEvent, message=TextMessage)
def comfort_bot(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        comfort_word= ComfortBot(event.message.text)
        
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= comfort_word)
        )

if __name__ == "__main__":
    app.run()