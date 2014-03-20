#!/usr/bin/python

import os, binascii, sys, getopt
import time, string, random

hexPrefix = ['06','46','C6','86']

'''
Generate keys into hex combination
'''
def generate_hex():
    return random.choice(hexPrefix) + binascii.b2a_hex(os.urandom(14)).upper()

'''
Generate keys into cd-key format combination
'''    
def generate_cdkey(size=24, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

'''
Create file based on the # of given files
'''
def create_file(files, combinations):
    for i in range(int(files)):
        fileName = "file" + str(i) + ".txt"
        fo = open(fileName, "wb")
        fo.write( "Python is a great language.\nYeah its great!!\n");
        fo.close()

'''
Main Call
'''
def main(argv):
    # Start reading parameters
    try:
      opts, args = getopt.getopt(argv,"hf:c:",["fileTotal=","combTotal="])
    except getopt.GetoptError:
      print 'generate.py -f <fileTotal> -c <combTotal>'
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print 'generate.py -f <fileTotal> -c <combTotal>'
         sys.exit()
      elif opt in ("-f", "--fileTotal"):
         fileTotal = arg
      elif opt in ("-c", "--combTotal"):
         combTotal = arg

    # Create files
    create_file(fileTotal, combTotal)     
    print fileTotal
    print combTotal

if __name__ == "__main__":
   main(sys.argv[1:])
