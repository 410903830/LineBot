import os
from dotenv import load_dotenv
load_dotenv()

##########
from Colth import *
from size import *
import image
import json
import random


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


#變數

size_mode = 'off'

 
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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'


# Message event						#這邊是用來接收訊息的地方
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	# events.message.type：這裡記錄訊息的型態
    # events.sourse.userId：這裡記錄使用者的ID
    reply_token = event.reply_token
    message = event.message.text	


    global size_mode
    #身高輸入
    if message == "身高輸入":
        size_mode = "height"
        line_bot_api.reply_message(reply_token, TextSendMessage(text="請輸入身高"))
    elif(size_mode == "height"):
        size_mode = "weight"
        size.height =message
        line_bot_api.reply_message(reply_token, TextSendMessage(text="請輸入體重"))
    elif (size_mode == "weight"):
        content = size.size(size.height, size.weight)
        line_bot_api.reply_message(reply_token, TextSendMessage(text= content))
        size_mode = "off"
    #體重輸入
    
    
    #使用者傳送的文字變數
    	
    
    if message == "你好":
        line_bot_api.reply_message(reply_token, TextSendMessage(text="你好啊"))
    #elif message =="身高輸入":

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
        line_bot_api.reply_message(reply_token, TemplateSendMessage(alt_text='ConfirmTemplate',template=Temp))
    elif message == "男裝":


        content, array = Colth.Menlink()
        imageutl =""
        columns=[]

        cloth_len = Colth.cloth_len

        random_count = random.sample(array, 5)

        
        for count in random_count:
            imageutl = count['image']
            colum= CarouselColumn(
                thumbnail_image_url=imageutl,
                title=count['title'],
                text=count['price'],
                actions=[
                URIAction(
                    label='點擊',
                    uri=count['url']
                    )
                ]
                )       
            columns.append(colum)
            
        Temp = CarouselTemplate(columns=columns)

        

        line_bot_api.reply_message(reply_token, TemplateSendMessage(alt_text='Carousel_Template',template=Temp))
    elif message == "優惠活動":
        content, array = Colth.Salelink()
        imageutl =""
        columns=[]
        random_count = random.sample(array, 5)

        for count in random_count:
            imageutl = count['image']
            colum= CarouselColumn(
                thumbnail_image_url=imageutl,
                title= count['title'],
                text= count['price'],
                actions=[
                URIAction(
                    label='點擊',
                    uri= count['url']
                    )
                ]
                )       
            columns.append(colum)
            
        Temp = CarouselTemplate(columns=columns)

        

        line_bot_api.reply_message(reply_token, TemplateSendMessage(alt_text='Carousel_Template',template=Temp))
    elif message == "功能":
        message_content = {
        "type": "text", 
        "text": "請選擇需要的服務",
        "quickReply": { 
        "items": [
        {
            "type": "action",
            "imageUrl": "https://example.com/sushi.png",
            "action": {
            "type": "message",
            "label": "尺寸",
            "text": "身高輸入"
            }
        },
        {
            "type": "action",
            "imageUrl": "https://example.com/tempura.png",
            "action": {
            "type": "message",
            "label": "男裝",
            "text": "男裝"
            }
        },
        {
            "type": "action", 
            "action": {
            "type": "location",
            "label": "Send location"
            }
        }
        ]
        }
    }
        line_bot_api.reply_message(reply_token, TextSendMessage.new_from_json_dict(message_content))

 


    else:
        line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
    

@handler.add(MessageEvent, message= ImageMessage)
def handleEvent(event):
    print(event.message.type)

    reply_token = event.reply_token
    #line_bot_api.reply_message(reply_token, TextSendMessage(alt_text='Text_Template',text=translate_text(message)))


    image_content = line_bot_api.get_message_content(event.message.id)
    image_name = event.message.id+'.jpg'
    path='./LineBot/static/'+image_name
    with open(path, 'wb') as fd:
        for chunk in image_content.iter_content():
            fd.write(chunk)

    base= image.encode_image(path)
    text= image.image_chat(base)

    line_bot_api.reply_message(reply_token, TextSendMessage(alt_text='Text_Template', text= text))
    
  


import os							# 這裡是指定我們的BOT執行的位置
if __name__ == "__main__":			
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)		# 我們的BOT會接收訊息的位置也就是 0.0.0.0:80/callback


