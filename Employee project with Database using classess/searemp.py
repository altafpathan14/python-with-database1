import oracledb as orc
from oracledb import DatabaseError
import sys

class searchemp:
    def __init__(self):
        number = int(input("Enter Employee Number to search employee:"))
        if (number <= 0):
            print("eno must be greater than 0")
            sys.exit()
        else:
            self.eno=number
            self.empser()
    def empser(self):
          try:
              conn=orc.connect("system/toor@localhost/xe")
              cur=conn.cursor()
              sq="select eno from employee where(eno=%d)"
              cur.execute(sq %(self.eno))
              records=cur.fetchone()
              if(records==None):
                  print("+" * 60)
                  print("\t\t\t\t----->Employee doesn't exist")
                  print("+" * 60)
              else:
                  print("+"*60)
                  print("\t\t\t\t---->Employee exist")
                  print("+" * 60)
          except orc.DatabaseError as db:
              print("problem in database:",db)




#main program
#s1=searchemp()

