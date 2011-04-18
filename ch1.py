
"""
This script takes the message from problem pychallenge problem 01 and translate it.
Translate method is letter + 2
Example using my name:
AFYB will translate to CHAD 

I'm doing this entire challenge in python3, I had an error message spit out at me ( still got the correct answer though ) that string.maketrans() has been deprecated and I should instead be using bytes.maketrans(). Noted.
"""
from string import maketrans # Imports the required maketrans module

message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj." # The message to be translated.

tranin = b'abcdefghijklmnopqrstuvwxyz' # The standard alphabet to use as the footing for the translation
tranout = b'cdefghijklmnopqrstuvwxyzab' # The alphabet according to the message. I.E how it was written

tranmeth = maketrans(tranin, tranout) #Simplicity is golden. Doing this just makes the following print function loook oh so pretty and short.

print(message.translate(tranmeth)) #And we get the message!
