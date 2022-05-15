import requests
from bs4 import BeautifulSoup
from loguru import logger

# url = 'https://mathom.es/es/2507-ofertas?orderby=name&orderway=desc&id_category=2507&n=1022'
# r = requests.get(url)
# with open("response.txt", "w") as f:
#     f.write(r.text)
# file_output = open("output.txt", "a")
# with open('response.txt') as f:
#     r = f.read()
# soup = BeautifulSoup(r, 'html.parser')
# MATHOM
def mathon_request():
    data = []
    items = 100
    link = 'https://mathom.es/es/2507-ofertas?orderby=name&orderway=desc&id_category=2507&n='
    r = requests.get(link+str(100))
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.find(id="nb_item").contents[7].text
    r = requests.get(link+items)
    soup = BeautifulSoup(r.text, 'html.parser')
    for container in soup.find_all("div", {"class": "pro_second_box"}):
        head = container.find("a")
        title = head["title"]
        url = head["href"]
        price = float(container.find("span",class_="price product-price").text[:-1].replace(",","."))
        try:
            old_price = float(container.find("span",class_="old-price product-price").text[:-1].replace(",","."))
        except:
            old_price = price
        available = container.find("div",class_="availability product_stock_info mar_b6").contents[1].text
        available = ''.join(available.split())
        data.append({"Title":title,"Price":price,"Old_Price":old_price,"Discount":(old_price-price)/old_price,"Available":available,"URL":url})
        ##### print(title + " /// " + url + " /// " + price + " /// " + old_price + " /// " + available, file=file_output)
    logger.debug("Mathom -> " + str(len(data)))
    return data
if __name__ == "__main__":
    data = mathon_request()
    print(len(data))
