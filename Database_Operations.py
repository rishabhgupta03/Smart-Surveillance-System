import sqlite3
import pandas as pd

class database:
    def record_input(self, uid, name, email,phone,pin):
        self.uid = int(uid)
        self.name = str(name)
        self.email = str(email)
        self.phone = int(phone)
        self.status=0
        self.pin=int(pin)

        conn = sqlite3.connect("SURVEILLANCE_SYSTEM.db")
        crsr = conn.cursor()
        crsr.execute("""INSERT INTO USER(uid, name,email,phone,status)
        VALUES(?,?,?,?,?)
        """, (self.uid , self.name ,self.email , self.phone , self.status))

        crsr.execute("""INSERT INTO CREDENTIALS(uid,pin)
                VALUES(?,?)
                """, (self.uid,self.pin))
        conn.commit()
        conn.close()

    def verify(self, uid,pin=0):
        self.uid = int(uid)
        self.pin= int(pin)
        if(self.find_record(self.uid)):
            conn = sqlite3.connect("SURVEILLANCE_SYSTEM.db")
            crsr = conn.cursor()
            crsr.execute("select uid,pin from CREDENTIALS")
            check = crsr.fetchall()
            conn.commit()
            conn.close()
            for a in check:
                if self.uid == a[0] and self.pin==a[1]:
                    return True
        return False

    def find_record(self,uid):
        self.uid = int(uid)
        conn = sqlite3.connect("SURVEILLANCE_SYSTEM.db")
        crsr = conn.cursor()
        crsr.execute("select uid from CREDENTIALS")
        check = crsr.fetchall()
        conn.commit()
        conn.close()
        for a in check:
            if self.uid == a[0] :
                return True
        return False


    def set_status(self,uid,status):
        self.uid=uid
        self.status=status

        conn = sqlite3.connect("SURVEILLANCE_SYSTEM.db")
        crsr = conn.cursor()
        crsr.execute(""" UPDATE USER SET status=? WHERE uid=? """,(self.status,self.uid))
        conn.commit()
        conn.close()



    def set_all_status(self):
        conn = sqlite3.connect("SURVEILLANCE_SYSTEM.db")
        crsr = conn.cursor()
        crsr.execute(""" UPDATE USER SET status=0 """)
        conn.commit()
        conn.close()

    def extract_email(self):
        conn = sqlite3.connect("SURVEILLANCE_SYSTEM.db")
        crsr = conn.cursor()
        crsr.execute(""" SELECT status,email FROM USER """)
        records = crsr.fetchall()
        conn.commit()
        conn.close()
        print(records)
        for a in records:
            if a[0]==1:
                return str(a[1])
        return False



    def display(self):

        conn = sqlite3.connect("SURVEILLANCE_SYSTEM.db")
        crsr = conn.cursor()
        crsr.execute("""Select * FROM USER""")
        records = crsr.fetchall()
        data = [[]] * len(records)

        data = [[records[i][0], records[i][1],records[i][2],records[i][3],records[i][4] ] for i in range(0, len(records))]
        print(pd.DataFrame(data, columns=["U_ID", "Name", "Email_ID","Phone_No","Status"]))

        conn.commit()
        conn.close()


