#!/usr/bin/python

"""
Challenge 6 script. Same as challenge 4, only with a zip file and not a url. 
"""

import zipfile
import re

rawZip = zipfile.ZipFile("./data/channel.zip", "r")
nothing = 90052
passCount = 1
pattern = re.compile('\d{2,5}')
coms = []
while passCount < len(rawZip.namelist()):
		for fileName in rawZip.namelist():
				zFile = str(nothing) + ".txt"
				data = rawZip.read(zFile).decode('utf-8') #has to be decoded, in raw form is byte data
				nothing ="".join(pattern.findall(data))
				coms.append(rawZip.getinfo(zFile).comment.decode())
				print(data)
				passCount += 1
				if nothing == '':
						break

print(''.join(coms))
