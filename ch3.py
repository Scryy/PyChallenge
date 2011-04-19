"""
Imports the data from a file and uses a regular expression to pick out the characters and output them. 

Side note: I'm aware I over commented the fuck out of this

For those keen enough to notice from the previous scripts doc: Yes I did just build off the last one
"""

import re   #Imports the required regular expression module

pattern = re.compile('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]') #Defines the regex object to be used

#Optional method of loading the file. Just substitude /path/to/file with 'f' sans the ''
#f = input('Enter path to file: ')

file = open('/path/to/file', 'r')
data = file.read() #Loads that entire mess into one string
file.close()

initial_output = list(pattern.findall(data)) #Parse using aforementioned regex object
final = [] #Stuff the output into a list for further parsing

for x in initial_output:  #Simple for loop to grab what we need
  final.append(x[4])

print(''.join(final)) #Aaaaaannnnddd ze output.
