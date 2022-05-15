import requests
from bs4 import BeautifulSoup
from loguru import logger

def jugamosuna_request():
# JUGAMOSUNA
    data = []
    link = 'https://jugamosuna.es/tienda/1618-rebajas?q=Disponibilidad-En+stock&page='
    page = 1
    while(True):
        r = requests.get(link+str(page))
        soup = BeautifulSoup(r.text, 'html.parser')
        logger.debug("Scrapping page: " + str(page))
        if soup.find(class_ ="page-content page-not-found") != None:
            logger.debug("None page found")
            break 
        for container in soup.find(class_= "products row").find_all(class_ = "product-description"):
            head = container.find("h3").find("a")
            title = head.contents[0]
            url = head["href"]
            price = float(container.find("span",class_="price").text[:-1].replace(",","."))
            try:
                old_price = float(container.find("span",class_="regular-price").text[:-1].replace(",","."))
            except:
                old_price = price
            pass
            data.append({"Title":title,"Price":price,"Old_Price":old_price,"Discount":(old_price-price)/old_price,"Available":"Enstock","URL":url})
        page+=1
    logger.debug("Jugamos Una -> " + str(len(data)))
    return data
if __name__ == "__main__":
    data = jugamosuna_request()
    print(len(data))