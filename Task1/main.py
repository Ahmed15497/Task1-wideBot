# -*- coding: utf-8 -*-
"""

@author: ahmed
"""
import time
from functions import take_url


url = input("Enter your url: ") 
substr = 'https://en.wikipedia.org'
url_chain = []
url_chain.append(url)
i = 0
max_iter = 500
if substr in url:
                
    a = take_url(url)
    time.sleep(0.5)
    
    if a != 1:
        while(a != 0 and a !=1):
            a = take_url(a)
            time.sleep(0.5)
            if type(a) == str:
                url_chain.append(a)
            i+=1
            if i == max_iter:
                print('Search has taken so long, I got tired')
                break;
    else:
        print(url)
else:
    print('It is not a wikipedia link!!!!')