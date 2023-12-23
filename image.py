import base64
import requests
import os
from dotenv import load_dotenv
load_dotenv()

# OpenAI API Key
api_key = os.getenv("api_key")

# 將圖片解碼成utf-8
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  

#base64_image = encode_image('boy.jpg')


def image_chat(base64_image):

  headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

  payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "這剛圖片的穿衣風格"
        },
        {
          "type": "image_url",
          "image_url": {
          "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 20
}

  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

  text = response.json()['choices'][0]['message']['content']


  print(text)

  return text