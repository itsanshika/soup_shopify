# This is a sample Python script.
from typing import Any

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup, ResultSet
import json


def Product_Info(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html5lib')
    f = open("/tmp/PageContent.html", 'w')
    f.write(req.content.decode())
    f.close()
    Data_ID = soup.find_all('span', attrs={'class': 'stamped-product-reviews-badge stamped-main-badge'})
    data = {
     "productId" : '7557336006850',
     "productName" : 'Bar+Necklace+Silver+-+Hanne',
     "productSKU" : 'bar-necklace-silver-hanne',
     "apiKey" : 'pubkey-yLiAU08oKVX27Ka7886R6dyf5oE0RN',
     "Id" : '12175',
     "page" : 10
    }
    return data




def Review_Info(productId,productName,productSKU,apiKey,Id,page):

  Review_List = []

  for x in range(page):

    Page = str(x)
    review_Url='https://stamped.io/api/widget?productId='+productId+'&productName='+productName+'&productSKU='+productSKU+'&page='+Page+'&apiKey='+apiKey+'&sId='+Id+'&take=5&widgetLanguage=en'


    r = requests.get(review_Url)
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

        # print(Created , Author, Location, Content)
        data = {
            "REVIEWER_PROFILE": Author,
            "RATING": "NULL",
            "REVIEW_CONTENT": Content,
            "REVIEW_DATE": Created
        }
        Review_List.append(json.dumps(data))

    # Use a breakpoint in the code line below to debug your script.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    url = 'https://www.linjer.co/collections/last-chance-sale/products/circle-necklace-silver-elsa'
    Info = Product_Info(url)

    print(Info)

    productId='7557336006850'
    productName='Bar+Necklace+Silver+-+Hanne'
    productSKU='bar-necklace-silver-hanne'
    apiKey='pubkey-yLiAU08oKVX27Ka7886R6dyf5oE0RN'
    Id='12175'
    page=10
    Review_Info(productId,productName,productSKU,apiKey,Id,page)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
