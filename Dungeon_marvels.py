from loguru import logger
import requests
from bs4 import BeautifulSoup
def dugeonmarvels_request():
# DUNGEON MARVELS
    data = []
    link = 'https://dungeonmarvels.com/217-super-ofertas?q=Disponibilidad-En+stock&page='
    page = 1
    while(True):
        r = requests.get(link+str(page))
        # with open("response.txt", "w") as f:
        #     f.write(r.text)
        # soup = BeautifulSoup(r.text, 'html.parser')
        # with open('response.txt') as f:
        #     r = f.read()
        soup = BeautifulSoup(r.text, 'html.parser')
        logger.debug("Scrapping page: " + str(page))
        if soup.find(class_ ="page-content page-not-found") != None:
            logger.debug("None page found")

            break
        for container in soup.find("div",class_="products row").find_all("div",class_="product-description"):
            head = container.find("h2").find("a")
            title = head.contents[0]
            url = head["href"]
            price = float(container.find("span",class_="price").text[:-1].replace(",","."))
            try:
                old_price = float(container.find("span",class_="regular-price").text[:-1].replace(",","."))
            except:
                old_price = price
            data.append({"Title":title,"Price":price,"Old_Price":old_price,"Discount":(old_price-price)/old_price,"Available":"Enstock","URL":url})
        page+=1
    logger.debug("Dungeons Marvels -> " + str(len(data)))
    return data
if __name__ == "__main__":
    data = dugeonmarvels_request()
    print(len(data))