import oracledb as orc
import sys
class delemp:
        def __init__(self):
            number = int(input("Enter Employee Number to search employee:"))
            if (number <= 0):
                print("eno must be greater than 0")
                sys.exit()
            else:
                self.eno = number
                self.empser()

        def empser(self):
            try:
                conn = orc.connect("system/toor@localhost/xe")
                cur = conn.cursor()
                sq = "select eno from employee where(eno=%d)"
                cur.execute(sq % (self.eno))
                records = cur.fetchone()
                if (records == None):
                    print("employee doesn't exist")
                else:
                    val=records[0]
                    dq="delete from employee where eno=%d"
                    cur.execute(dq %(val))
                    conn.commit()
                    print("{} record deleted".format(cur.rowcount))
            except orc.DatabaseError as db:
                print("problem in database:",db)
#s1=delemp()