from loguru import logger
import requests
from bs4 import BeautifulSoup
def link(page):
    return 'https://zacatrus.es/juegos-de-mesa.html?outlet2=1755&p='+ str(page)+ '&product_list_limit=36'
def zacatrus_request():
# Zacatrus
    data = []
    page = 1
    while(True):
        r = requests.get(link(page))
        soup = BeautifulSoup(r.text, 'html.parser')
        logger.debug("Scrapping page: " + str(page))
        if soup.find(class_ ="message info empty") != None:
            logger.debug("None page found")
            break
        for container in soup.find_all('li', class_= "item product product-item"):
            head = container.find("a", class_= "product-item-link")
            title = head.contents[0]
            title = ' '.join(title.split())
            url = head["href"]
            try:
                price = float(container.find("span",class_="special-price").find("span",class_="price").text[:-1].replace(",","."))
            except:
                try:
                    price = float(container.find("span",class_="price-container price-final_price tax weee").find("span",class_="price").text[:-1].replace(",","."))
                except:
                    continue
            try:
                old_price = float(container.find("span",class_="old-price").find("span",class_="price").text[:-1].replace(",","."))
            except:
                old_price = price
            data.append({"Title":title,"Price":price,"Old_Price":old_price,"Discount":(old_price-price)/old_price,"Available":"Enstock","URL":url})
        page+=1
    logger.debug("Zacatrus Tienda -> " + str(len(data)))
    return data
if __name__ == "__main__":
    data = zacatrus_request()
    print(len(data))