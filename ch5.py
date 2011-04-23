"""
Script outputs the answer in a unix style banner. Should be pretty self explanatory
I wrote the output to a file rather than a console because I wrote this under my windows install, in which I still haven't setup gVIm to invoke the python intrepeter
and I sure as fuck wasn't staring at the ouput from that joke they call the command prompt.
"""

import pickle
import sys

sys.stdout = open('data/banner.txt', 'w')
file = open('data/banner.p', 'rb')
file_output = pickle.load(file)
for line in file_output:
  print(''.join(map(lambda x: x[0]*x[1], line)))
