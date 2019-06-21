# -*- coding: utf-8 -*-
"""

@author: ahmed
"""


import requests
from bs4 import BeautifulSoup
import urllib

substr = 'https://en.wikipedia.org'


def take_url(url):
    if (substr in url):
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        header = soup.find(id='firstHeading').text
        full_link = None
        
        if header != 'Philosophy':
            
            content = soup.find(id='mw-content-text')
        
            for element in content.find_all("p"):
                if element.find("a"):
                    article_link = element.find("a").get('href')
                    full_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
                    print(full_link)
                    break
                
            if full_link != None:
                return full_link
            else:
                print("Can not find links in this webpage")
                return 0
                
        else:
            return 1
    else:
        print('It is not a wikipedia link !!!!')
        return 0
            
    
            