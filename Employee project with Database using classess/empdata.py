import oracledb as orc
import sys
class emplo:
    def __init__(self):
        number=int(input("Enter Employee Number to get details:"))
        if(number<=0):
            print("eno must be greater than 0")
            sys.exit()

        self.eno=number
        self.empget()
    def empget(self):
        try:
            conn=orc.connect("system/toor@localhost/xe")
            cur=conn.cursor()
            cnq="select eno from employee where(eno=%d)"
            cur.execute(cnq %(self.eno))
            record=cur.fetchone()
            if(record==None):
                print("Employee does't exist:")
            else:
                val=record[0]
                sq = "select *  from employee where(eno=%d)"
                cur.execute(sq % (val))
                for colnames in cur.description:
                    print(colnames[0], end="\t\t")
                print()
                record = cur.fetchone()
                for val in record:
                    print(val, end="\t\t")

        except orc.DatabaseError as db:
            print("Error in:",db)
        print()

#main project
#s1=emplo()
