from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class":"bhgxx2 col-12-12"})                                    
filename = "products.csv"
f = open(filename,"w")
headers = "Phone_Name,Price,User_Rating\n"
f.write(headers)
print("LIST OF IPHONES")
for i in range(2,26) :
    container = containers[i]
    Phone_Name = container.div.img["alt"]
    price = container.find("div",{"class":"_1vC4OE _2rQ-NK"})
    Price = price.text
    rating = container.find("div",{"class":"hGSR34"})
    User_Rating = rating.text
    print(Phone_Name.replace(",","-")+","+Price+","+User_Rating+"\n")
    f.write(Phone_Name.replace(",","-")+","+Price+","+User_Rating+"\n")