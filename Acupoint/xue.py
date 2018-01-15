# -*-coding:utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup

def getHTML(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


if __name__ == '__main__':
    url = 'http://www.360doc.com/content/15/0128/21/8541396_444561649.shtml'
    html = getHTML(url)

    # comp = re.findall(r'style="TEXT-ALIGN: center; MARGIN: 0px auto; FONT-WEIGHT: bold">\d*.+',html)
    # print len(comp)
    # jingmai = re.findall(r'>\d(.+)<',comp[0])[0].encode('utf-8')
    #
    # with open('test1.txt', 'a+') as f:
    #     for item in comp:
    #         f.write(re.findall(r'>\d*(.+)<', item)[0].encode('utf-8') + '\n')

    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    with open('test2.txt', 'w+') as f:
        for item in a:
            href = item.attrs['href']
            if re.compile('http://www.taozhy.com/ShuJuKu/XueWei/\d+.thtml').match(href):
                f.write(href.encode('utf-8') + '\t' + item.string.encode('utf-8') + '\n')
                print href
                print item.string