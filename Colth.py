import requests
import random
from bs4 import BeautifulSoup


class Colth:


    cloth_len = 0


    #男裝   
    def Menlink():

        random_number = random.randint(0, 6)
        url= f'https://www.efshop.com.tw/category/457/{random_number}'
        web = requests.get(url)
        soup = BeautifulSoup(web.text, "html.parser")

        content = ""
        array = []

    
        colth = soup.findAll( class_='idx_pro2')

        cloth_len = len(colth)


        for i in range(1, len(colth)):
            price = colth[i].find(class_ = 'monenyBig').get_text()
            url = colth[i].find('a')['href']
            image = colth[i].find('img')['src']
            title = colth[i].find('a')['title']
            content +=f"{price}{image}"+"\n"
            array.append({'title':title, 'price':price, 'image':image, 'url':url})
    
        return content, array
    
    #女裝
    def Womenlink():

        random_number = random.randint(1, 12)
        url= f'https://www.efshop.com.tw/category/21/{random_number}'
        web = requests.get(url)
        soup = BeautifulSoup(web.text, "html.parser")

        content = ""
        array = []

    
        colth = soup.findAll( class_='idx_pro2')


        for i in range(1, len(colth)):
            price = colth[i].find(class_ = 'monenyBig').get_text()
            url = colth[i].find('a')['href']
            image = colth[i].find('img')['src']
            title = colth[i].find('a')['title']
            content +=f"{price}{image}"+"\n"
            array.append({'title':title, 'price':price, 'image':image, 'url':url})
    
        return content, array
    
    #優惠
    def Salelink():

        url= 'https://www.efshop.com.tw/category/957/1'
        web = requests.get(url)
        soup = BeautifulSoup(web.text, "html.parser")

        content = ""
        array = []

    
        colth = soup.findAll( class_='idx_pro2')


        for i in range(1, len(colth)):
            price = colth[i].find(class_ = 'monenyBig').get_text()
            url = colth[i].find('a')['href']
            image = colth[i].find('img')['src']
            title = colth[i].find('a')['title']
            content +=f"{price}{image}"+"\n"
            array.append({'title':title, 'price':price, 'image':image, 'url':url})
    
        return content, array
    
    #選擇 


    """
    
    男性/上衣類/4
    https://www.efshop.com.tw/category/487

    男性/下身/1
    https://www.efshop.com.tw/category/488

    男性/運動衣褲/2
    https://www.efshop.com.tw/category/496
    

    女性/上衣類/17
    https://www.efshop.com.tw/category/1

    女性/下身/8
    https://www.efshop.com.tw/category/72

    女性/運動衣褲/7
    https://www.efshop.com.tw/category/266
    

    """


    #search_Cloth
    def Search_Cloth(gender, cloth_type):

        print(f"{gender}{cloth_type} 從Cloth.py 讀取")

        random_number = ""
        url = ""

        if gender=="男性" and cloth_type=="上衣":

            number=4
            url=f'https://www.efshop.com.tw/category/487'

        elif gender=="男性" and cloth_type=="下身":

            number=1
            url=f'https://www.efshop.com.tw/category/488'

        elif gender=="男性" and cloth_type=="運動衣褲":

            number=2
            url=f'https://www.efshop.com.tw/category/496'

        elif gender=="女性" and cloth_type=="上衣":

            number=17
            url=f'https://www.efshop.com.tw/category/1'

        elif gender=="女性" and cloth_type=="下身":

            number=8
            url=f'https://www.efshop.com.tw/category/72'

        elif gender=="女性" and cloth_type=="運動衣褲":

            number=7
            url=f'https://www.efshop.com.tw/category/266'

        else:
            return ""

        random_number = random.randint(1, number)


        url = f'{url}/{random_number}'


        web = requests.get(url)
        soup = BeautifulSoup(web.text, "html.parser")

        content = ""
        array = []
        colth = soup.findAll( class_='idx_pro2')


        print(len(colth))

        for i in range(1, len(colth)):
            price = colth[i].find(class_ = 'monenyBig').get_text()
            url = colth[i].find('a')['href']
            image = colth[i].find('img')['src']
            title = colth[i].find('a')['title']
            content +=f"{price}{image}"+"\n"
            array.append({'title':title, 'price':price, 'image':image, 'url':url})


    
        return content, array


