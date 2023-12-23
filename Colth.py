import requests
from bs4 import BeautifulSoup


class Colth:

    def Menlink():

        url= 'https://www.efshop.com.tw/category/461/1'
        web = requests.get(url)
        soup = BeautifulSoup(web.text, "html.parser")

        content = ""
        array = []

    
        colth = soup.findAll( class_='idx_pro2')


        for i in range(1, len(colth)):
            price = colth[i].find(class_ = 'monenyBig').get_text()
            image = colth[i].find('img')['src']
            content +=f"{price}{image}"+"\n"
            array.append({'image':image})
    
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
            image = colth[i].find('img')['src']
            content +=f"{price}{image}"+"\n"
            array.append({'image':image})
    
        return content, array
    

