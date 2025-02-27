import oracledb as orc

class updateemp:
    def __init__(self):
        while(True):
            self.eno = int(input("Enter Employee Number which u want to update:"))
            self.nsal = float(input("Enter new salary:"))
            self.ncom = input("Enter new company name:")
            self.updatemp()
            print("----------------------------------------------")
            ch = input("do u want to insert another record(yes/no):")
            if (ch.lower() == "no"):
                print("thx for updating")
                break
    def updatemp(self):
            try:
                conn = orc.connect("system/toor@localhost/xe")
                cur = conn.cursor()
                uq = "update employee set sal=%f,company='%s' where eno=%d"

                cur.execute(uq %(self.nsal,self.ncom,self.eno))
                conn.commit()
                if(cur.rowcount>0):
                    print("{}  record updated".format(cur.rowcount))
                else:
                    print("Employee record doesn't exist")

            except orc.DatabaseError as db:
                print("problem in database:",db)
            except ValueError:
                print("Don't enter str, alnums, syumbols ")

#s1=updateemp()

