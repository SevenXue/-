# -*- coding:utf-8 -*-

import  re
import requests
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def getHTML(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

with open('test2.txt', 'r') as f:
    lines = f.readlines()
    with open('acupoint.csv', 'w') as wf:
        for i in range(len(lines)):

            url = lines[i].split('\t')[0]
            name = lines[i].split('\t')[1].strip()
            print url, name

            html = getHTML(url)
            soup = BeautifulSoup(html, 'html.parser')
            divcon = soup.find('div', attrs={'id': 'PanelContent'})
            print divcon

            if 1:
                #获取所属脉络
                vein = soup.find_all('span', attrs={'style': 'font-weight:bold;'})[1].contents[0]
                info_str = str(i+1) + ',' + name + ',' + vein
                print vein

                #获取解剖，疾病，定位，url
                info_dict = {}
                for item in divcon.contents:
                    info = item.encode('utf-8').split('】')

                    if info[0] == '【解剖':
                        info_dict[1] = info[-1]
                    if info[0] == '【定位' or info[0] == '【位置':
                        info_dict[3] = info[-1]

                    if info[0] == '【主治' or info[0] == '【功效':
                        info_dict[2] = info[-1]

                if 1 in info_dict.keys():
                    info_str += ',' + info_dict[1]
                    #print type(info_dict[1])
                    #info.append(info_dict[1])
                else:
                    info_str += ',' + ''
                    #info.append('null')
                if 2 in info_dict.keys():
                    #info_str += ',' + info_dict[3]
                    #info.append(info_dict[2])
                    #info.append('null')
                    info_str += ',' + info_dict[2] + ',' + ''
                else:
                    info += ',' + '' + ',' + ''
                    #info.append('null')
                    #info.append('null')
                if 3 in info_dict.keys():
                    #info.append(info_dict[3])
                    info_str += ',' + info_dict[3]
                else:
                    info += ',' + ''
                    #info.append('null')
                info_str += ',' + url + '\n'

                print info_str
                wf.write(info_str)