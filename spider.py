from bs4 import BeautifulSoup
import requests

from prettytable import PrettyTable

import time

x = PrettyTable()
x.field_names = ["Name", "Price", "Time Left"]

# List of item names to search on eBay
name_list = ["lego ninjago"]

item_name = []
prices = []
times = []


# Returns a list of urls that search eBay for an item
def make_urls(names):
    # eBay url that can be modified to search for a specific item on eBay
    url = "https://www.ebay.de/sch/i.html?_from=R40&_nkw=" # "https://www.ebay.de/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=" # 
    # List of urls created
    urls = []

    for name in names:
        # Adds the name of item being searched to the end of the eBay url and appends it to the urls list
        # In order for it to work the spaces need to be replaced with a +
        urls.append(url + name.replace(" ", "+") + "&_sacat=0&LH_TitleDesc=0&_sop=1")

    # Returns the list of completed urls
    return urls


# Scrapes and prints the url, name, and price of the first item result listed on eBay
def ebay_scrape(urls):
    for url in urls:
        # Downloads the eBay page for processing
        res = requests.get(url)
        # Raises an exception error if there's an error downloading the website
        res.raise_for_status()
        # Creates a BeautifulSoup object for HTML parsing
        soup = BeautifulSoup(res.text, 'html.parser')


        ###
        listings = soup.find_all('li', attrs={'class': 's-item'})
        prod_name=" "
        prod_price = " "
        prodTimeLeft = " "
    
        for listing in listings:

            for name in listing.find_all('h3', attrs={'class':"s-item__title"}):

                if(str(name.find(text=True, recursive=False))!="None"):
                    prod_name=str(name.find(text=True, recursive=False))
                    item_name.append(prod_name)

                    price = listing.find('span', attrs={'class':"s-item__price"})
                    prod_price = str(price.find(text=True, recursive=False))
                    prices.append(prod_price)

                    time = listing.find('span', attrs={'class':"s-item__time-left"})
                    if (time != None):
                        prodTimeLeft = str(time.find(text=True, recursive=False))
                    else:
                        prodTimeLeft = "-"
                    times.append(prodTimeLeft)

            x.add_row([prod_name, prod_price, prodTimeLeft])
    print(x)

# Runs the code
# 1. Make the eBay url list
# 2. Use the returned url list to search eBay and scrape and print information on each item
start = time.time()
ebay_scrape(make_urls(name_list))
end = time.time()
print(end - start)
