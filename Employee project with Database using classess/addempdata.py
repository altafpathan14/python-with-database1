import oracledb as orc
class adddata:
        def __init__(self):
            while (True):
                print("Enter Employee Details:-")
                print("-" * 50)
                self.eno = int(input("Enter Employee Number:"))
                self.ename = input("Enter Employee Name:")
                self.sal = float(input("Enter Employee Salary:"))
                self.cname = input("Enter Company Name:")
                self.connection()
                ch = input("Do you wanna Add Another Emp Data? (yes/no):")
                if (ch.lower() == "no"):
                    print("Thanks For Adding:-")
                    break

        def connection(self):
            try:
                conn = orc.connect("system/toor@localhost/xe")
                cur = conn.cursor()

                iq = "insert into employee values(%d,'%s',%f,'%s')"
                cur.execute(iq % (self.eno, self.ename, self.sal, self.cname))
                conn.commit()
                print("{} Row Created".format(cur.rowcount))
                print("Employee Data inserted into DataBase--verify")
                print("---------------------------------------------")

            except orc.DatabaseError as db:
                print("The problem in DataBase:--")

#main program
#s1=adddata()


