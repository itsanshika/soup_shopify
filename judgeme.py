# This is a sample Python script.
import json
from typing import Any

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import requests
from bs4 import BeautifulSoup, ResultSet



def Product_Info(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html5lib')
    f = open("/tmp/PageContent.html", 'w')
    f.write(req.content.decode())
    f.close()
    productid = soup.find('span', attrs={'class': 'shopify-product-reviews-badge'})['data-id']
    data = {
        "productId": productid,
        "url" : 'plumgoodness-2.myshopify.com',
        "page": 10
    }
    return data

def Review_Info(productid,url,page):

    Review_List = []

    for x in range(page):
        Page = str(x)
        review_Url = 'https://judge.me/reviews/reviews_for_widget?url='+url+'&shop_domain='+url+'&platform=shopify&page='+Page+'&per_page=5&product_id=' + productid
        r = requests.get(review_Url)
        r_decode = r.content.decode()
        review_page = r_decode.encode().decode("unicode-escape")

        soup = BeautifulSoup(review_page, 'html5lib')

        tables = soup.find_all('div', attrs={'class': 'jdgm-rev jdgm-divider-top'})
        for table in tables:
            Content = table.find('div', attrs={'class': 'jdgm-rev__body'}).find('p').text
            Review = table.find('span', attrs={'class': 'jdgm-rev__rating'})
            Review=Review['data-score']
            name = table.find('span', attrs={'class': 'jdgm-rev__author'}).text
            date = table.find('span', attrs={'class': 'jdgm-rev__timestamp jdgm-spinner'})
            date=date['data-content']
            data = {
                "REVIEWER_PROFILE": name,
                "RATING": Review,
                "REVIEW_CONTENT": Content,
                "REVIEW_DATE": date
            }
            Review_List.append(json.dumps(data))







if __name__ == '__main__':


    url='https://plumgoodness.com/products/phy-vitamin-sea-mint-sea-kelp-energizing-body-wash'
    Info= Product_Info(url)
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html5lib')
    f = open("/tmp/JudgeMe.html", 'w')
    f.write(req.content.decode())
    f.close()



    productid= soup.find('span',attrs={'class':'shopify-product-reviews-badge'})['data-id']
    url='plumgoodness-2.myshopify.com'
    page=10

    Review_Info(productid,url,page)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
