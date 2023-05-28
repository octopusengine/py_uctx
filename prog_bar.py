#!/usr/bin/env python3
"""
simple test: 2018/02
progressbar:
$ pip3 install tqdm
"""

import os, sys
from tqdm import tqdm


param = sys.argv[1]

if param == "-h":
   print("[ help ]")
   print("Brute force search for a prime number")
   print("(Only simple python example)")
   print("Single parameter: your number") # 123123123 / 3,9,123,369,1001001,3003003,....
   print()

else:

  try:
    numi = int(param)
    deli = 2
    prime = True
    print("[ divisions ]")

    for num in tqdm(range(numi-2)):
       if (numi%deli==0):
           print(deli, end=" | ")
           prime = False
       deli = deli+1

    if prime: print("none")
    print()
    print("Number:", numi, end=" ")
    if prime: print("is prime.")

  except:
    print('[ err ]')
    print("Parameter must be a number.")

  print()
  print("[ end ]")
