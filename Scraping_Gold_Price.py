import csv
import requests
import bs4
from datetime import datetime as dt
import os

# task is to scrape gold price and time from https://markets.businessinsider.com/commodities/gold-price and save it in csv
def get_gold_price():
    page = requests.get("https://markets.businessinsider.com/commodities/gold-price")
    soup = bs4.BeautifulSoup(page.text, "html.parser")
    price = soup.find("span", {"class":"price-section__current-value"}).text
    print('The current price is {} USD'.format(price))
    return price

def write_to_csv(price):
    DATE_FORMAT = '%d.%m.%Y %H:%M'
    if "gold_price.csv" in os.listdir():
        mode = "a"
    else:
        mode = "w"
    f = open("gold_price.csv", mode)
    f_writer = csv.writer(f)
    f_writer.writerow([price,dt.now().strftime(DATE_FORMAT)])
    f.close()
print(write_to_csv(get_gold_price()))



#MY VERY NOOB VERSION
#prices = []
#print(soup)
#list_of_prices = (soup.find_all("div", class_="markets-now__current-value"))
#gold = list_of_prices[3]
#gold_str = str(gold)
#numbers = []
#for word in str(gold_str.split()):
#    if word.isdigit():
#        numbers.append(int(word))
#print(numbers)
#new_str = ""
#for number in numbers:
#    new_str += str(number)

#print(new_str[:4],".",new_str[4:], "USD")
