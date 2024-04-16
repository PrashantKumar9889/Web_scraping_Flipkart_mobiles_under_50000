import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(1,12):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(1)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find('div', class_ = "_1YokD2 _3Mn1Gg")

    names = box.find_all('div', class_= "_4rR01T")
    for i in names:
        name = i.text
        Product_name.append(name)

    price = box.find_all('div', class_ = "_30jeq3 _1_WHN1")
    for i in price:
        pr = i.text
        Prices.append(pr)
    print(len(Prices))

    desc = box.find_all('ul', class_ ="_1xgFaf")
    for i in desc:
        de = i.text
        Description.append(de)
    print(Description)    

    review = box.find_all('div', class_ ="_3LWZlK")
    for i in review:
        re = i.text
        Reviews.append(re)
    print(len(Reviews))

df = pd.DataFrame({"Product Name":Product_name, "Prices":Prices, "Descripation":Description, "Reviews":Reviews})
print(df)         

df.to_csv('Flipkart_Mobiles_under_50000.csv')