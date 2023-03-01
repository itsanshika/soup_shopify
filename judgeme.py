# This is a sample Python script.
from typing import Any

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup, ResultSet

def Reviws_Data(productid):
    urlpage3 = 'https://judge.me/reviews/reviews_for_widget?url=plumgoodness-2.myshopify.com&shop_domain=plumgoodness-2.myshopify.com&platform=shopify&page=3&per_page=5&product_id='+productid
    urlpage6 = 'https://judge.me/reviews/reviews_for_widget?url=zilch-cosmetics.myshopify.com&shop_domain=zilch-cosmetics.myshopify.com&platform=shopify&page=2&per_page=5&product_id='+productid
    r = requests.get(urlpage3)
    x = r.content.decode()
    x.encode()
    y = x.encode().decode("unicode-escape")

    soup = BeautifulSoup(y, 'html5lib')
    f = open("/tmp/judgeme.html", 'w')
    f.write(y)
    f.close()
    tables = soup.find_all('div', attrs={'class': 'jdgm-rev jdgm-divider-top'})
    for table in tables:
        Content = table.find('div', attrs={'class': 'jdgm-rev__body'}).find('p').text
        print(Content)
        Review = table.find('span', attrs={'class': 'jdgm-rev__rating'})
        print(Review['data-score'])
        content = table.find('span', attrs={'class': 'jdgm-rev__author'}).text
        print(content)
        date = table.find('span', attrs={'class': 'jdgm-rev__timestamp jdgm-spinner'})
        print(date['data-content'])


if __name__ == '__main__':

    url6 = 'https://zilchcosmetics.com/collections/face/products/afterglow?variant=33427662733445'
    url3='https://plumgoodness.com/products/phy-vitamin-sea-mint-sea-kelp-energizing-body-wash'
    req = requests.get(url1)
    soup = BeautifulSoup(req.content, 'html5lib')
    f = open("/tmp/JudgeMe.html", 'w')
    f.write(req.content.decode())
    f.close()

    productid= soup.find('span',attrs={'class':'shopify-product-reviews-badge'})['data-id']
    Reviws_Data(productid)

    # print(Data_ID)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
