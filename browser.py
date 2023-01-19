
import sys
import os, requests
from bs4 import BeautifulSoup
from colorama import Fore
#
args = sys.argv
dir = args[1]
if not os.access(dir, os.F_OK):
    os.mkdir(dir)

list =[]
while True:
    url = input()
    if not '.' in url:

        if url == 'exit':
            break
        elif url == 'back':
            if len(list) != (0):
                print(open(f'{dir}/{list[-2]}', 'r', encoding='UTF-8').read())
        else:
            print('Invalid URL')
    else:
        if not url.startswith('https://'):
            nurl = 'https://' + url
        r = requests.get(nurl)
        soup = BeautifulSoup(r.content, 'html.parser')
        hlist = soup.find_all(['h1', 'h2', 'p', 'ul', 'ol', 'li'])
        alist = soup.find_all('a')
        file = open(f'{dir}/{url.split(".")[0]}', 'w', encoding="utf-8")
        for i in (hlist, alist):
            for j in i:
                if i == hlist: print(j.text)
                elif i == alist: print(Fore.BLUE + j.text)
                file.write(j.text + '\n')
        file.close
        list.append(url.split(".")[0])

        

