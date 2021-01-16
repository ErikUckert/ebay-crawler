import requests as requests
from bs4 import BeautifulSoup
item_name = []
prices = []
 
for i in range(1,10):
 
    ebayUrl = "https://www.ebay.com/sch/i.html?_from=R40&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;_nkw=note+8&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;_sacat=0&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;_pgn="+str(i)
    r= requests.get(ebayUrl)
    data=r.text
    soup=BeautifulSoup(data, features="html.parser")
 
    listings = soup.find_all('li', attrs={'class': 's-item'})
 
    for listing in listings:
        prod_name=" "
        prod_price = " "
        for name in listing.find_all('h3', attrs={'class':"s-item__title"}):
            if(str(name.find(text=True, recursive=False))!="None"):
                prod_name=str(name.find(text=True, recursive=False))
                item_name.append(prod_name)
 
        if(prod_name!=" "):
            price = listing.find('span', attrs={'class':"s-item__price"})
            prod_price = str(price.find(text=True, recursive=False))
            prod_price = int(sub(",","",prod_price.split("INR")[1].split(".")[0]))
            prices.append(prod_price)
 
from scipy import stats
import numpy as np
import pandas as pd
 
data_note_8 = pd.DataFrame({"Name":item_name, "Prices": prices})
data_note_8 = data_note_8.iloc[np.abs(stats.zscore(data_note_8["Prices"]))&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;lt; 3,]