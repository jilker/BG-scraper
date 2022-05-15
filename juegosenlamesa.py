from loguru import logger
import requests
from bs4 import BeautifulSoup
def juegosenlamesa_request():
# DUNGEON MARVELS
    data = []
    link = 'https://juegosenlamesa.com/collections/ofertas?page='
    page = 1
    while(True):
        r = requests.get(link+str(page))
        soup = BeautifulSoup(r.text, 'html.parser')
        logger.debug("Scrapping page: " + str(page))
        if soup.find(class_ ="grid__item one-whole center") != None:
            logger.debug("None page found")
            break
        for container in soup.find("div",class_= "page-width collection-product-list").find_all("div",class_ ="product-block"):
            head = container.find("div",class_ = "product-block__title").find("a")
            title = head.contents[0]
            url = "https://juegosenlamesa.com" + head["href"]
            try:
                price = container.find("span",class_="product-price__reduced theme-money").text
            except:
                price = container.find("span",class_="theme-money").text
            price = float(''.join(price.split())[1:].replace(",","."))
            try:
                available = container.find("span",class_="product-label product-label--on-sale global-border-radius").text
            except:
                available = "Duda"
            available = ''.join(available.split())
            try:
                old_price = container.find("span",class_="product-price__reduced theme-money").text
                old_price = float(''.join(old_price.split())[1:].replace(",","."))
            except:
                old_price = price
            data.append({"Title":title,"Price":price,"Old_Price":old_price,"Discount":(old_price-price)/old_price,"Available":available,"URL":url})
        page+=1
    logger.debug("Juegos en la mesa -> " + str(len(data)))
    return data
if __name__ == "__main__":
    data = juegosenlamesa_request()
    print(len(data))