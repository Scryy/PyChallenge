#!/usr/bin/python3
#The urllib module has changed in Python3 read up on it here: http://docs.python.org/release/3.0.1/search.html?q=Urllib&check_keywords=yes&area=default


import urllib.request   
import re

pattern = re.compile('\d{2,5}') #Not every number is 5 digits long, but there's a page or two with a single digit so best to account for all them between 2 and 5 digits long

pass_count = 1 #Counter for the for loop

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = 12345

while pass_count < 10000:  #10k is just a randomly long number to use to account for the while loop
  require = urllib.request.urlopen(url + str(nothing)) #Eachtime this is called a new url gets created and opened, per the conditions of the current 'nothing' and the initial url.
  page = require.read().decode("utf-8") #page had to be converted into a string so that I could worth with the data. I really dind't feel like fucking with byte code for this
  print('Current nothing is:', nothing, page)
  nothing = ''.join(pattern.findall(page)) #Isolate the numbers
  pass_count += 1 #Increase the counter

"""
The if statement:

Without the first line the program would just continuously loop until it reached a count of 10k. 

My first few times running the script I kept noticing the the sentence popping up but really didn't feel like writing in a function or method to catch it. I caught it ( by stopping the script via ctrl+c ) and was fed this message:
  61066 There maybe misleading numbers in the text. One example is 61067. Look only for the next nothing and the next nothing is 53522

The third line is just to continue going once youn reach the first answer. ( yes you get several )
"""

if nothing == '':
    break
  if nothing == '6106753522':
     nothing = 53522
  elif nothing =='92118':
     nothing = 46059

