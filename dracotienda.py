from loguru import logger
import requests
from bs4 import BeautifulSoup
def dracotienda_request():
# DUNGEON MARVELS
    data = []
    link = 'https://dracotienda.com/1879-ofertas?page='
    page = 1
    while(True):
        r = requests.get(link+str(page))
        soup = BeautifulSoup(r.text, 'html.parser')
        logger.debug("Scrapping page: " + str(page))
        if soup.find(class_ ="page-content page-not-found") != None:
            logger.debug("None page found")
            break
        for container in soup.find("div",id="js-product-list").contents[1].find_all("div",class_= "laber-product-description"):
            head = container.find("h2").find("a")
            title = head.contents[0]
            url = head["href"]
            price = float(container.find("span",class_="price").text[:-1].replace(",","."))
            available = container.find("span",class_="product-availability").text
            available = ''.join(available.split())
            try:
                old_price = float(container.find("span",class_="regular-price").text[:-1].replace(",","."))
            except:
                old_price = price
            data.append({"Title":title,"Price":price,"Old_Price":old_price,"Discount":(old_price-price)/old_price,"Available":available,"URL":url})
        page+=1
    logger.debug("Draco Tienda -> " + str(len(data)))
    return data
if __name__ == "__main__":
    data = dracotienda_request()
    print(len(data))