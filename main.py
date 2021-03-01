import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

request = requests.get(alba_url)
soup = BeautifulSoup(request.txt, "html.parser")

brand = soup.find("div", {"id": "MainSuperBrand"}).find_all("li", {"class": "impact"})

for b in brand:
  row = b.find("a", {"class": "goodsBox-info"})
  brand_name = row.find("span", {"class" : "company"})

  file = open(f"{brand_name}.csv", mode = "w")
  writer = csv.writer(file)
  writer.writerow("palce", "title", "time", "pay", "date")

  link = row["href"]
  request = requests.get(link)
  link_soup = BeautifulSoup(request.txt , "html.parser")

  # scrapping alba

  t = link_soup.find("table")
  rows = t.find_all("tr")
  for row in rows:
    place = row.find("td", {"class":"local"})
    if place != None:
      place = place.text
      title = row.find("td",{"class":"title"}).find("span", {"class":"company"}).text
      tm = row.find("td", {"class" : "data"}).find("span").text
      pay = row.find("td", {"class": "pay"}).find("span", {"class" : "payIcon"}).text + row.find("td", {"class": "pay"}).find("span", {"class": "number"}).text
      dt = row.find("td", {"class" : "regDate"}).text

      writer.writerow([place, title, tm, pay, dt])


    