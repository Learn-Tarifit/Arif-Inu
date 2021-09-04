url = "https://wold.clld.org/values/"

from list import d
import requests
from bs4 import BeautifulSoup

with open("output.py", 'w', encoding='utf-8') as file:
    for i in range(len(d)):
        tarifit_word = d[i]["tf"]
        english_word = BeautifulSoup(requests.get(url + d[i]["en"]).content, "html.parser").find(class_="Parameter").text
        print(str(i) + ' {tf=%s, en=%s}' % (tarifit_word, english_word))
        file.write(f'["tf": "{tarifit_word}", "en": "{english_word}"],\n')