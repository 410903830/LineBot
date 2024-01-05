import os
#from dotenv import load_dotenv
#load_dotenv()

##########
from Colth import *
from size import *
import image
import json
import random
import Regular


from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import*
app = Flask(__name__)


#環境變數
#line_token = os.getenv("token")
#cannel_screte = os.getenv("screte")

line_token = "dHsa9nu14mQJ4BQyROTugbIsSlmpWghmFIHOZgDJBbSqKdZPqJl6uM0iOQetyxjJrZOhTBVhMex7uCj00zCEa1pOVeRCBXkOYrgiL7TfYh52XnDO2jkZgUIGQDv8qnadslXk8FQg2Mx73WceRQxnOAdB04t89/1O/w1cDnyilFU="
cannel_screte = "88d9337002cf903a0edd35e7c5811e05"

#LINE BOT infol
line_bot_api = LineBotApi(line_token) 
 #將Messaging manager中的Channel access token值填入
handler = WebhookHandler(cannel_screte)
 #basic setting中的Channel Secret值填入


#變數
size_mode = 'off'
gender = ''
cloth_type = ''
 
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
    user_id = event.source.user_id


    global size_mode
    global gender
    global cloth_type


    ######  抓取 designer json 
    myjsonfile = open('LineBot/disnger.json', 'r')
    jsondata = myjsonfile.read()
    obj= json.loads(jsondata)
    ######



    print(gender)
    print(cloth_type)


    #身高輸入
    if message == "身高輸入":
        size_mode = "height"
        line_bot_api.reply_message(reply_token, TextSendMessage(text="請輸入身高"))
    elif(size_mode == "height"):
        size_mode = "weight"
        size.height =message
        line_bot_api.reply_message(reply_token, TextSendMessage(text="請輸入體重"))
    #體重輸入
    elif (size_mode == "weight"):
        content = size.size(size.height, size.weight)
        if content=="S" or content=="M" or content=="M" or content=="L" or content=="XL" or content=="XXL" or content=="3XL":
            line_bot_api.reply_message(reply_token, TextSendMessage(text= f"你適合的尺寸是:{content}"))
        else:
            line_bot_api.reply_message(reply_token, TextSendMessage(text= content))   
        size_mode = "off"
    
    elif message == "挑選衣服":
        line_bot_api.reply_message(reply_token, FlexSendMessage(alt_text='FlexSendMessage',contents= obj['design'][4]))
        
    elif message=="男性" or  message=="女性":
        gender = message
        line_bot_api.reply_message(reply_token, FlexSendMessage(alt_text='FlexSendMessage', contents= obj['design'][3]))

    elif message=="上衣" or message== "下身" or message== "運動衣褲":
        cloth_type = message

        if gender== "男性" or gender== "女性":

            content, array= Colth.Search_Cloth(gender, cloth_type)

            imageutl =""
            columns=[]

            random_count = random.sample(array, 5)

            print(len(array))
            print(len(random_count))

        
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

        else:
            print(user_id)
        line_bot_api.reply_message(reply_token, FlexSendMessage(alt_text='FlexSendMessage',contents=obj['design'][4]))


    elif message == "服務地點":

        local = LocationSendMessage(
            title='快樂Go 衣芙',
            address='台中市沙鹿區快樂Go芙飾店',
            latitude=24.22670282531597,
            longitude= 120.57744879206233
        )
        line_bot_api.reply_message(reply_token, local)

    #男裝
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
    
        #男裝
    
    #女裝
    elif message == "女裝":


        content, array = Colth.Womenlink()
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
    
    #優惠活動
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
    
    #圖片辨識
    elif message == "chatgpt 圖片辨識":

        Temp = ConfirmTemplate(
            text= '請選擇圖片',
            actions=[
                CameraAction(
                    label='相機',
                ),
                CameraRollAction(
                    label='相簿'
                )
            ]
        )

        line_bot_api.reply_message(reply_token, TemplateSendMessage( alt_text="ConfirmTemplate", template=Temp))

    #功能
    elif message == "功能":

        line_bot_api.reply_message(reply_token, TextSendMessage.new_from_json_dict(obj['design'][5]))

    elif message == "test":

        line_bot_api.reply_message(reply_token, FlexSendMessage(alt_text="123",
        
        contents= obj['design'][1]
      
))

    elif message == "相機":
        template_message = TemplateSendMessage(
        alt_text='Camera Template',
        template=ButtonsTemplate(
            title='點擊相機拍攝',
            text=' ',
            actions=[
                CameraAction(label='相機')
            ]
        )
    )
        line_bot_api.reply_message(reply_token, template_message)

    elif message == "相簿":
        template_message = TemplateSendMessage(
        alt_text='Camera Template',
        template=ButtonsTemplate(
            title='點擊相簿開啟',
            text=' ',
            actions=[
                CameraRollAction(label='相簿')
            ]
        )
    )
        line_bot_api.reply_message(reply_token, template_message)

    #鸚鵡
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


    gender, style, color, text = Regular.Re(text)
    

    line_bot_api.reply_message(reply_token, TextSendMessage(alt_text='Text_Template', text= text))
    line_bot_api.reply_message(reply_token, TextSendMessage(alt_text='Text_Template', text= gender))
    line_bot_api.reply_message(reply_token, TextSendMessage(alt_text='Text_Template', text= style))
    line_bot_api.reply_message(reply_token, TextSendMessage(alt_text='Text_Template', text= color))
    
  


import os							# 這裡是指定我們的BOT執行的位置
if __name__ == "__main__":			
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)		# 我們的BOT會接收訊息的位置也就是 0.0.0.0:80/callback


