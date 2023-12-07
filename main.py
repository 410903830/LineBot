import os
from dotenv import load_dotenv
load_dotenv()


from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import*
app = Flask(__name__)


#環境變數

line_token = os.getenv("token")
cannel_screte = os.getenv("screte")


#LINE BOT infol
line_bot_api = LineBotApi(line_token) 
 #將Messaging manager中的Channel access token值填入
handler = WebhookHandler(cannel_screte)
 #basic setting中的Channel Secret值填入

 
@app.route("/callback", methods=['POST'])		
#指定在 /callback 通道上接收訊息，且方法是 POST
def callback():								
#callback()是為了要檢查連線是否正常
    signature = request.headers['X-Line-Signature'] 
    #signature是LINE官方提供用來檢查該訊息是否透過LINE官方APP傳送
    body = request.get_data(as_text=True)		
    #body就是用戶傳送的訊息，並且是以JSON的格式傳送
    app.logger.info("Request body: " + body)
    print(body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# Message event						#這邊是用來接收訊息的地方
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_type = event.message.type	# events.message.type：這裡記錄訊息的型態
    user_id = event.source.user_id		# events.sourse.userId：這裡記錄使用者的ID
    reply_token = event.reply_token
    
    
    
    #使用者傳送的文字變數
    message = event.message.text		
    
    if message == "你好":
        line_bot_api.reply_message(reply_token, TextSendMessage(text="你好啊"))
    elif message == "早安":
        line_bot_api.reply_message(reply_token, TextSendMessage(text="早安"))
    
    elif message == "服務地點":

        local = LocationSendMessage(
            title='快樂Go 衣服',
            address='台中市沙鹿區快樂Go服飾店',
            latitude=24.22670282531597,
            longitude= 120.57744879206233
        )
        line_bot_api.reply_message(reply_token, local)


    elif message == "1":

        Temp = ConfirmTemplate(
            
            text='你好嗎',
            actions=[
                MessageAction(
                    label='好喔',
                    text='好喔'
                ),
                MessageAction(
                    label='不太好',
                    text='不太好'
                )
            ]
        )
        line_bot_api.reply_message(reply_token, TemplateSendMessage(alt_text='ConfirmTemplate',
        template=ConfirmTemplate(
            text='你好嗎？',
            actions=[
                MessageAction(
                    label='好喔',
                    text='好喔'
                ),
                MessageAction(
                    label='不好喔',
                    text='不好喔'
                )
            ]
        )))


    else:
        line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
    
    

    #傳送image
    #image_url = 'https://i.imgur.com/dW8RTRj.jpg'
    #line_bot_api.reply_message(reply_token, ImageSendMessage(original_content_url=image_url, preview_image_url=image_url))     

    
    
    
    
    #line_bot_api.reply_message()是回傳訊息的方法，設定回傳的型態是文字(text)
	#而我們接收到的訊息會被放在event中，一樣會是JSON格式

import os							# 這裡是指定我們的BOT執行的位置
if __name__ == "__main__":			
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)		# 我們的BOT會接收訊息的位置也就是 0.0.0.0:80/callback