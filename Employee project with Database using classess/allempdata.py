import oracledb as orc
class allemp:
    def __init__(self):
            try:
                conn=orc.connect("system/toor@localhost/xe")
                cur=conn.cursor()
                iq="select * from employee"
                cur.execute(iq)
                for colum in cur.description:
                    print(colum[0],end="\t\t")
                print()
                records=cur.fetchall()
                for record in records:
                    for val in record:
                        print(val,end="\t\t")
                    print()


            except orc.DatabaseError as db:
                print("problem in database:",db)



#main program
#s1=allemp()