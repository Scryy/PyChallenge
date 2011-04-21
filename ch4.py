#!/usr/bin/python3
#The urllib module has changed in Python3 read up on it here: http://docs.python.org/release/3.0.1/search.html?q=Urllib&check_keywords=yes&area=default


import urllib.request   
import re

pattern = re.compile('\d{2,5}') #Not every number is 5 digits long, but there's a page or two with a single digit so best to account for all them between 2 and 5 digits long

pass_count = 1 #Counter for the for loop

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = 12345

while pass_count < 10000:
  require = urllib.request.urlopen(url + str(nothing))
  page = require.read().decode("utf-8")
  print('Nothing pass', str(pass_count),':', nothing, page)
  nothing = ''.join(pattern.findall(page))
  pass_count += 1

  if nothing == '':
    break
  if nothing == '6106753522':
     nothing = 53522
  elif nothing =='92118':
     nothing = 46059

