"""
This is some ugly code that does not conform to PEP 8.

Check me with pycodestyle:
    pycodestyle ../resources/pep8_example.py
"""
from string import *
import math, os, sys

def f(x):
    """This function has lines that are just too long. The maximum suggested line length is 80 characters."""
    return 4.27321*x**3  -8.375134*x**2  + 7.451431*x + 2.214154 - math.log(3.42153*x) + (1 + math.exp(-6.231452*x**2))
def g(x,
     y):
    print("Bad splitting of arguments")

# examples of bad spacing
mydict  =  { 'ham' : 2,  'eggs'  : 7  }#this is badly spaced
mylist=[ 1 , 2 , 3 ]

myvar   = 7
myvar2  = myvar*myvar
myvar10 = myvar**10

# badly formatted math
a= myvar+7 *  18-myvar2  /  2

l = 1 # l looks like 1 in some fonts
I = l # also bad
O = 0 # O looks like 0 in some fonts
