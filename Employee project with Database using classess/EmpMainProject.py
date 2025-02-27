from menu import mainmenu
from addempdata import adddata
from allempdata import allemp
from empdata import emplo
from searemp import searchemp
from deleteemp import delemp
from updateEmp import updateemp
import sys
while(True):
    try:
        mainmenu()
        ch=int(input("Enter your choice:"))
        match(ch):
            case 1:
               add=adddata()
            case 2:
                d = delemp()
            case 3:
                up=updateemp()
            case 4:
                s=emplo()
            case 5:
                s1=allemp()
            case 6:
                s2= searchemp()
            case 7:
                sys.exit()
            case _:
                print("your selection of operation wrong try again")
    except ValueError:
        print("Don't Enter str,alnums and symbols")


