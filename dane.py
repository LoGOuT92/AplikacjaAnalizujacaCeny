from bs4 import BeautifulSoup
import requests
class Dane:
    def dane(self):
        URL='https://r.jakumo.org/prices.php'
        page = requests.get(URL)
        bs=BeautifulSoup(page.content,'html.parser')
        tablica=[]
        tables = bs.find('table',class_='table table-hover')
        for tr in tables.find_all("tr"):
            for td in tr.find_all("td"):
                tablica.append(td.text.replace(' ',''))
        return tablica
