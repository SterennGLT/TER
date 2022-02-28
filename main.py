# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3


connection = sqlite3.connect("base1.db")

cursor = connection.cursor()

#cursor.execute("create table etudiant (char nom, integer age)")
#cursor.execute("insert into etudiant values ('didier',23)")
#typ = cursor.execute("select * from etudiant")

#for n in typ:
#    print(n)

#cursor.execute("insert into answers_free values (4,'charles')")
#typ = cursor.execute("select * from answers_free")

#for n in typ:
#   print(n)

   
typ = cursor.execute("select * from users")
for n in typ:
    print(n)

connection.commit()
#for row in cursor.execute('SELECT * FROM answers_free'):
    #print(row)


connection.close()