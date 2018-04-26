
import sqlite3
import time
from datetime import datetime
#from databaseQueries import *
'''
timestamp_s = '2:56 13/3/2018'
timestamp_o = datetime.strptime(timestamp_s, "%H:%M %d/%m/%Y")
print(timestamp_o.__dict__)
timestamp_u = timestamp_o.strftime("%s")
print(int(timestamp_u))
'''
sqlite_file = 'propAcaFriends2.sqlite'
conn = sqlite3.connect(sqlite_file)
cursor = conn.cursor()
#cursor.execute(create_ctrs_tab)


create_ctrs_tab = 'SELECT population\n'
create_ctrs_tab += 'FROM countries\n'
create_ctrs_tab += 'WHERE population < 1000000;\t\n'
'''
'''
create_ctrs_tab = 'INSERT INTO afternoonFriends \n (Content, Created)'
create_ctrs_tab += '\nVALUES \n("Sirinya", "2:56 13/3/2018");'
print(create_ctrs_tab)
cursor.execute(create_ctrs_tab)
conn.commit()

all_rows = cursor.fetchall()
print(all_rows)

conn.close()

