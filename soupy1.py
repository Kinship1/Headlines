from bs4 import BeautifulSoup
import requests
import pandas as pd
from pprint import pprint
import os


def get_page(url=''):
    if url:
        try:
            page = requests.get(url)    # gets the page
            if page.status_code == 200:    # 200 is success code similar to 404- which is page not found
                # create soup object
                soup = BeautifulSoup(page.text,"lxml")
                return soup
            else:
                print('could not be found',page.url)
                print("error--->",page.status_code)
        except Exception as e:
            print('fatal error',e)
            print('check internet or web address')
            print('the url',url)
    else:
        print("must provide a valid url with HTTP protocol")


file1 = open("type.txt")
types = file1.read()
url = "https://www.hindustantimes.com/"
url = url + types
print(url)
soup = get_page(url)

head = soup.find_all(attrs={"class":"media-body"})
data = []
for i,headlines in enumerate(head):
    headings = headlines.find('a').text.strip()
    para = headlines.find(attrs={'class':'para-txt'})
    if para == None:
        para = headlines.find('p')
    if para == None:
        continue
    else:
        data.append({
            'Heading': headings,
            'Paragraph': para.text.strip()
        })

pd.DataFrame(data).to_csv('htnews.csv')
print('done,check current folder')
columns = ['Heading','Paragraph']
df = pd.read_csv("htnews.csv")
df.drop(columns='Unnamed: 0', inplace=True)
df = df.dropna()
html = df.to_html()

for direct in os.scandir():
    if direct.name == 'templates':
        tem_dir = direct.path
with open(os.path.join(tem_dir,'mypage.html'),"w", encoding="utf-8") as file:
    msg = "<link rel='stylesheet' type='text/css' href='{{ url_for('static',filename='style1.css') }}'>"
    file.write(msg)
    file.write(html)
