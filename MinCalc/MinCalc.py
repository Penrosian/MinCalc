from math import *
from sys import *

def cryoMixerToImpact(mixers):
    return((mixers*12)//15)

def blastMixerToImpact(blastMixers):
    return(int((blastMixers*0.75)//(1/2.33)))

def pyraFacToBlastFac(pyraFacs):
    return(int((pyraFacs*2.25)//3))

def blastFacToImpact(blastFacs):
    return(int((blastFacs*2.25)//(1/2.33)))

def ask():
    asked = int(input("What would you like to calculate?\n(1) Cryofluid mixers to impact reactors\n(2) Blast mixers to impact reactors\n(3) Pyratite factories(Exogenesis) to blast factories(Exogenesis)\n(4) Blast factories(Exogenesis) to impact reactors\n(5) Pyratite factories(Exogenesis) to impact reactors\n"))
    if asked == 1:
        print("You can run", str(cryoMixerToImpact(int(input("How many cryofluid mixers? ")))), "reactors.")
    elif asked == 2:
        print("You can run", str(blastMixerToImpact(int(input("How many blast mixers? ")))), "reactors.")
    elif asked == 3:
        print("You can run", str(pyraFacToBlastFac(int(input("How many pyratite factories? ")))), "blast factories.")
    elif asked == 4:
        print("You can run", str(blastFacToImpact(int(input("How many blast factories? ")))), "reactors.")
    elif asked == 5:
        print("You can run", str(blastFacToImpact(pyraFacToBlastFac(int(input("How many pyratite factories? "))))), "reactors.")
    for x in range(3):
        print("")
    ask()
        
ask()
