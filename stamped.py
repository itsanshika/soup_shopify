# This is a sample Python script.
from typing import Any

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup, ResultSet
import json

# url1='https://www.linjer.co/collections/last-chance-sale/products/circle-necklace-silver-elsa'



def print_hi(productId,productName,productSKU,apiKey,Id):
  for x in range(20):
    page = str(x)
    # url2 = 'https://stamped.io/api/widget?productId='+ProductId+'&productName=Circle%20Necklace%20Silver%20-%20Elsa&productSKU=circle-necklace-silver-elsa&page='+page+'&apiKey=pubkey-yLiAU08oKVX27Ka7886R6dyf5oE0RN&sId=12175&take=5&widgetLanguage=en'
    # url3 = 'https://stamped.io/api/widget?productId=7126723690682&productName=TreeBlend+Classic+T-Shirt&productType=Womens&productSKU=TCW2455-0016-XS&page='+page+'&apiKey=pubkey-LO1Xa8x73gKEGHN3Wryy0ivU11p2tu&sId=32040&take=5&sort=recent&widgetLanguage=en'
    url4='https://stamped.io/api/widget?productId='+productId+'&productName='+productName+'&productSKU='+productSKU+'&page='+page+'&apiKey='+apiKey+'&sId='+Id+'&take=5&widgetLanguage=en'


    r = requests.get(url4)
    soup=BeautifulSoup(r.content,'html5lib')
    f=open("/tmp/review.html", 'w')
    f.write(r.content.decode())
    f.close()

    tables = soup.find_all('div', attrs={'class': '\\"stamped-review\\"'})

    # print(tables)


    for table in tables:

        Created = table.find('div', attrs={'class': '\\"created\\"'}).text
        Author=table.find('strong', attrs={'class': '\\"author\\"'}).text
        Location= table.find('div', attrs={'class': '\\"review-location\\"'}).text
        Content= table.find('p', attrs={'class': '\\"stamped-review-content-body\\"'}).text

        # print(Created , Author, Location, Content)
        data = {
            "REVIEWER_PROFILE": Author,
            "RATING": "NULL",
            "REVIEW_CONTENT": Content,
            "REVIEW_DATE": Created
        }
        print(json.dumps(data))


    # Use a breakpoint in the code line below to debug your script.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    url1 = 'https://www.linjer.co/collections/last-chance-sale/products/circle-necklace-silver-elsa'
    url2='https://www.tentree.com/collections/womens-best-sellers/products/womens-basic-tee-white'
    req = requests.get(url1)
    soup = BeautifulSoup(req.content, 'html5lib')
    f = open("/tmp/PageContent.html", 'w')
    f.write(req.content.decode())
    f.close()


    Data_ID = soup.find_all('span', attrs={'class': 'stamped-product-reviews-badge stamped-main-badge' })

    # Api_Key= soup.find_all('form',attrs={'id':'new-question-form', 'class':'new-question-form'})
    # Api_Key = soup.find('section', attrs={'id' : 'shopify-section-template--15977704227010__reviews'})
    # Info=Api_Key.find('div', attrs={'class':'stamped-main-widget'})
    # children = Info.findChildren("div", attrs={'class':'stamped-container'})
    # keys = Api_Key.find_all('div', attrs={'class':'stamped-container'})

    # print_hi(Info['data-product-id'])
    # print(Data_ID)
    # print(Info['data-name'])
    # print(Info['data-product-id'])
    # print(Api_Key)
    productId='7557336006850'
    productName='Bar+Necklace+Silver+-+Hanne'
    productSKU='bar-necklace-silver-hanne'
    apiKey='pubkey-yLiAU08oKVX27Ka7886R6dyf5oE0RN'
    Id='12175'
    print_hi(productId,productName,productSKU,apiKey,Id)


    # for data in Info:
    #      print(data)
    #      Reviews=data.find('span',attrs={'class': 'stamped-badge'})
    #      print(Reviews)
    # CountReviews=Info.find('span', attrs={'class':'stamped-badge-caption'}).text
    # print(CountReviews)
    # for table in tables:
    #     Created = table.find('div', attrs={'class': '\\"created\\"'}).text



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
