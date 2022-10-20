#!/usr/bin/python3

from bs4 import BeautifulSoup
import re

html = open('coverage/index.html')
soup = BeautifulSoup(html, 'html.parser')
data = str(soup.findAll(attrs={'strong'}))
output = [int(s) for s in re.findall(r'\b\d+\b', str(data))]
print(all(flag == 100 for (flag) in output))
