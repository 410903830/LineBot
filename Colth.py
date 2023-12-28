import requests
from bs4 import BeautifulSoup


class Colth:


    cloth_len = 0

    def Menlink():

        url= 'https://www.efshop.com.tw/category/461/1'
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
    

