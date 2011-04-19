"""
Imports the data from a file and uses a regular expression to pick out the characters and output them. 

Side note: I'm aware I over commented the fuck out of this
"""

import re   #Imports the required regular expression module

pattern = re.compile('[a-zA-Z]') #Defines the regex object to be used

#Optional method of loading the file. Just substitude /path/to/file with 'f' sans the ''
#f = input('Enter path to file: ')

file = open('/path/to/file/', 'r')
data = file.read() #Loads that entire mess into one string
file.close()

output = pattern.findall(data) #Parse using aforementioned regex object

print(''.join(output)) #Print into a string otherwise output would be a list. Which is ugly. 

