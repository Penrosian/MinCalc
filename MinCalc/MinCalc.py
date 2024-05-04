from math import *
from sys import *

def cryoToImpact(mixers):
    return((mixers*12)//15)

def pyraFacToBlastFac(pyraFacs):
    return(int((pyraFacs*2.25)//3))

def ask():
    asked = int(input("What would you like to calculate?\n(1) Cryofluid mixers to impact reactors\n(2) Pyratite factories(Exogenesis) to blast compound factories(Exogenesis)\n"))
    if asked == 1:
        print("You can run", str(cryoToImpact(int(input("How many cryofluid mixers? ")))), "reactors.")
    elif asked == 2:
        print("You can run", str(pyraFacToBlastFac(int(input("How many pyratite factories? ")))), "BC factories.")
    for x in range(3):
        print("")
    ask()
        
ask()
