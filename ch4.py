#!/usr/bin/python3
import urllib.request
import re

pattern = re.compile('\d{2,5}')
pass_count = 1
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = 12345

while pass_count < 10000:
  require = urllib.request.urlopen(url + str(nothing))
  page = require.read().decode("utf-8")
  print('Current nothing is:', nothing, page)
  #new_num=int(   ''.join(pattern.findall(page)))
 #nothing = str(new_num / 2)
  nothing = ''.join(pattern.findall(page))
  pass_count += 1

  if nothing == '':
    break
  if nothing == '6106753522':
     nothing = 53522
  elif nothing =='92118':
     nothing = 46059

