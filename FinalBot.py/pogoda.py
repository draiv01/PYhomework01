import requests
from bs4 import BeautifulSoup
import re


def spb(curr_name):
    url = 'https://yandex.ru/pogoda/saint-petersburg?lat=59.938951&lon=30.315635'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html')

    quotes = soup.find_all('span')
    print(quotes)
    for i in range(len(quotes)):
        if curr_name.capitalize() == quotes[i].text:
            ind_el = i
            return (quotes[ind_el + 1].text)
    return ("не верный формат!")

