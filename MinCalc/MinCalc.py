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

def surgeCalc(silicon,copper,lead,titanium):
    global siliconRun
    global siliconExcess
    global copperRun
    global copperExcess
    global leadRun
    global leadExcess
    global titaniumRun
    global titaniumExcess
    siliconRun = silicon//2.4
    siliconExcess = round(silicon%2.4,1)
    copperRun = copper//2.4
    copperExcess = round(copper%2.4, 1)
    leadRun = lead//3.2
    leadExcess = round(lead%3.2, 1)
    titaniumRun = titanium//1.6
    titaniumExcess = round(titanium%1.6, 1)
    if (titaniumRun == leadRun) & (titaniumRun == copperRun) & (titaniumRun == siliconRun): return(1)
    else: return(0)

def ask():
    asked = int(input("What would you like to calculate?\n(1) Cryofluid mixers to impact reactors\n(2) Blast mixers to impact reactors\n(3) Surge production\n(4) Pyratite factories(Exogenesis) to blast factories(Exogenesis)\n(5) Blast factories(Exogenesis) to impact reactors\n(6) Pyratite factories(Exogenesis) to impact reactors\n"))
    if asked == 1:
        print("You can run", str(cryoMixerToImpact(int(input("How many cryofluid mixers? ")))), "reactors.")
    elif asked == 2:
        print("You can run", str(blastMixerToImpact(int(input("How many blast mixers? ")))), "reactors.")
    elif asked == 3:
        if surgeCalc(float(input("How much silicon production do you have? ")),float(input("How much copper production do you have? ")),float(input("How much lead production do you have? ")),float(input("How much titanium production do you have? "))) == 1:
            print("All resources are able to run the same number of surge smelters. Good job!\nResource excess:",titaniumExcess,"titanium,",leadExcess,"lead,",copperExcess,"copper, and",siliconExcess,"silicon.")
        else:
            print("Your resources are not in equilibrium. Your resources can run... Titanium:",int(titaniumRun),"Copper:",int(copperRun),"Lead:",int(leadRun),"Silicon:",int(siliconRun),"surge smelters.\nResource excess:",titaniumExcess,"titanium,",leadExcess,"lead,",copperExcess,"copper, and",siliconExcess,"silicon.")
    elif asked == 4:
        print("You can run", str(pyraFacToBlastFac(int(input("How many pyratite factories? ")))), "blast factories.")
    elif asked == 5:
        print("You can run", str(blastFacToImpact(int(input("How many blast factories? ")))), "reactors.")
    elif asked == 6:
        print("You can run", str(blastFacToImpact(pyraFacToBlastFac(int(input("How many pyratite factories? "))))), "reactors.")
    for x in range(3):
        print("")
    ask()
        
ask()
