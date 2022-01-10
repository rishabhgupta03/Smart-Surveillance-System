import sqlite3

conn =sqlite3.connect("SURVEILLANCE_SYSTEM.db")
crsr = conn.cursor()
crsr.execute("""CREATE TABLE USER(
                 uid integer(11),
                 name text,
                 email text,
                 phone integer(10),
                 status integer(1),
                 PRIMARY KEY(uid))""")
crsr.execute("""CREATE TABLE CREDENTIALS(
                uid integer(11),
                pin integer(8),
                FOREIGN KEY(uid) REFERENCES USER(uid))""")






conn.commit()
conn.close()