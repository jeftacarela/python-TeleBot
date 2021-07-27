import json
import requests
import re
from bs4 import BeautifulSoup

all_cookies = dict()
headers = dict()
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"

def get_cookies():
    global all_cookies

    f = open("data.json","r")
    cookiesData = f.read()
    f.close()

    cookiesData = json.loads(cookiesData)

    for i in cookiesData:
        name = i['name']
        value = i['value']
        all_cookies[name] = value

def connect_zomato():
    r = requests.get("https://www.zomato.com/",cookies=all_cookies,headers=headers)
    
    if("Log out" in r.text):
        print("Logged In")
    else:
        print("Invalid cookies")
    # print(r.text)

def scrapeResto():
    r = requests.get("https://www.zomato.com/jakarta/tebet-restaurants", headers=headers)

    soup = BeautifulSoup(r.text,"html.parser")
    divs = soup.find_all("div",{'class':'content'})
    # print(divs)


    for div in divs:
        restoName = div.findChildren("a",{'class':'result-title'})
        for name in restoName:
            n = name.contents[0]
            print(n)
        
        restoAddress = div.findChildren("div",{'class':'col-m-16'})
        for address in restoAddress:
            a = address.contents[0]
            print(a)
        
        restoRating = div.findChildren("span",{'class':'rating-value'})
        for rating in restoRating:
            r = rating.contents[0]
            print(r)
            print("----------------------")
        
        
        # print(restoName)
        # print(restoAddress)
        # print(restoRating)
get_cookies()
connect_zomato()
scrapeResto()
