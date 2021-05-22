from flask  import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

from linebot.models import MessageEvent, TextMessage, TextSendMessage

import configparser


from comforting_bot_for_loki import HandleReasons as ComfortBot


config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__, template_folder="templates")

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    
    body = request.get_data(as_text=True)
    app.logger.info("Request body:" + body)
    print(body)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    return 'OK'

#echo
#@handler.add(MessageEvent, message=TextMessage)
#def echo(event):
#    line_bot_api.reply_message(
#        event.reply_token,
#        TextSendMessage(text=event.message.text)
#        )

#med_bot
@handler.add(MessageEvent, message=TextMessage)
def comfort_bot(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        comfortReply= ComfortBot(event.message.text)
        
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= comfortReply)
        )

if __name__ == "__main__":
    
    app.run()
