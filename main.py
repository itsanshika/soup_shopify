# This is a sample Python script.
from typing import Any

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup, ResultSet

# url1='https://www.linjer.co/collections/last-chance-sale/products/circle-necklace-silver-elsa'



def print_hi():
  for x in range(6):
    page = str(x)
    url2 = 'https://stamped.io/api/widget?productId=7557345673410&productName=Circle%20Necklace%20Silver%20-%20Elsa&productSKU=circle-necklace-silver-elsa&page='+page+'&apiKey=pubkey-yLiAU08oKVX27Ka7886R6dyf5oE0RN&sId=12175&take=5&widgetLanguage=en'

    r = requests.get(url2)
    soup=BeautifulSoup(r.content,'html5lib')
    f=open("/tmp/review.html", 'w')
    f.write(r.content.decode())
    f.close()

    tables = soup.find_all('div', attrs={'class': '\\"stamped-review\\"'})
    for table in tables:
        Created = table.find('div', attrs={'class': '\\"created\\"'}).text
        Author=table.find('strong', attrs={'class': '\\"author\\"'}).text
        Location= table.find('div', attrs={'class': '\\"review-location\\"'}).text
        Content= table.find('p', attrs={'class': '\\"stamped-review-content-body\\"'}).text

        print(Created , Author, Location, Content)


    # Use a breakpoint in the code line below to debug your script.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    url1 = 'https://www.linjer.co/collections/last-chance-sale/products/circle-necklace-silver-elsa'
    req = requests.get(url1)
    soup = BeautifulSoup(req.content, 'html5lib')
    f = open("/tmp/PageContent.html", 'w')
    f.write(req.content.decode())
    f.close()


    # Data_ID = soup.find_all('span', attrs={'class': 'stamped-product-reviews-badge stamped-main-badge' })
    # Api_Key= soup.find_all('form',attrs={'id':'new-question-form', 'class':'new-question-form'})
    Api_Key = soup.find('section', attrs={'id' : 'shopify-section-template--15977704227010__reviews'})
    Info=Api_Key.find('div', attrs={'class':'stamped-main-widget'})
    children = Info.findChildren("div", attrs={'class':'stamped-container'})
    keys = Api_Key.find_all('div', attrs={'class':'stamped-container'})

    # print(Api_Key)
    # print(Info['data-name'])
    # print(Info['data-product-id'])
    print(Api_Key)
    # print_hi()


    # for data in Info:
    #      print(data)
    #      Reviews=data.find('span',attrs={'class': 'stamped-badge'})
    #      print(Reviews)
    # CountReviews=Info.find('span', attrs={'class':'stamped-badge-caption'}).text
    # print(CountReviews)
    # for table in tables:
    #     Created = table.find('div', attrs={'class': '\\"created\\"'}).text



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
