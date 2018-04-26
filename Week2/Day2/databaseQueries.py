
from SQLapp import TODOApp
import sqlite3
#sqlite_file = 'propAcaFriends4.sqlite'
friends = TODOApp('propAcaFriends2')

#friends.create_table('testTable')
#friends.add('afternoonFriends', 'Content, Created', '"Antoine", "4:07 13/3/2018"')
#friends.add('afternoonFriends', 'Content, Created', '"Sirinya", "2:56 13/3/2018"')


print(friends.search('*', 'afternoonFriends'))
#friends.addColumn('afternoonFriends', 'favouriteFood', 'text')
#friends.create_table_foreignKey()

#friends.create_table('eveningFriends', )
#friends.addColumn('eveningFriends', 'Dinner Plans', 'text')
#friends.addColumn('eveningFriends', 'Gym', 'binary')
#friends.addColumn('eveningFriends', 'TravelTime', 'text')
#friends.addColumn('eveningFriends', 'Name', 'text')
friends.insert('eveningFriends', 'Gym, TravelTime', '0, 120')

friends.create_table_foreignKey('nightFriends2', 'TODOid', 'foreignTableTest', 'TODOid')
