from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%'

#opening up connection
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html,"html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename,"w")
header = "brand,product_title,shipping\n"
f.write(header)

for container in containers:
    brand = container.div.div.a.img["title"]
    title_container = container.findAll("a",{"class":"item-title"})
    product_title = title_container[0].text
    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: "+brand)
    print("product_title : "+product_title)
    print("shipping : "+ shipping)
    f.write(brand + "," + product_title.replace(",","|") + "," + shipping + "\n")
f.close()