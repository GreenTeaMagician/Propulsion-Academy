
import sqlite3


class TODOApp:
	
		#works
	def create_table(self, name):
		self.cursor.execute(f"CREATE TABLE {name}\n(PrimKey integer PRIMARY KEY);")
		print(f'Table {name} created')
		
	def create_table_foreignKey(self, nativeTable, primaryKey, foreignTable, foreignKey):
		sqlquery = f"CREATE TABLE {nativeTable}(\n{primaryKey} integer PRIMARY KEY, FOREIGN KEY({foreignKey}) REFERENCES {foreignTable}({foreignKey}));"
		self.cursor.execute(sqlquery)
		print(f'Table {nativeTable} with Foreign Key {foreignKey} in {foreignTable} created')

		#works
	def __init__(self, db):
		self.db = db
		self.conn = sqlite3.connect(f"{self.db}.sqlite")
		self.cursor = self.conn.cursor()
		print(f'Database {db} created')
		
		#works
	def search(self, column, table):
		self.column = column
		self.table = table
		self.cursor.execute(f"SELECT {column}\nFROM {table}")
		return self.cursor.fetchall()
		
		#works
	def searchwc(self, column, table, constraint):
		self.cursor.execute(f"SELECT {column}\nFROM {table}\nWHERE {constraint}")
		return self.cursor.fetchall()
		
		#works
	def run(self, sqlScript):
		self.cursor.execute(sqlScript)
		self.conn.commit()
		return self.cursor.fetchall()
		
		#works
	def insert(self, table, columns, values):
		self.string = f'INSERT INTO {table} \n ({columns})\nVALUES \n({values});'
		self.cursor.execute(self.string)
		self.conn.commit()
		print("Entry Added")
		
		#works
	def delete(self, table, where):
		self.string = f'DELETE FROM {table}\n WHERE \n({where});'
		self.cursor.execute(self.string)
		self.conn.commit()
		print("Items deleted")
		
	def dropTable(self, table):
		i = input('Hang on... are you suuuure you want to drop this table? y/n\n')
		if  i=='y':
			i2 = input('Wait, really?\n')
			if i2  == 'y':
				self.string = f'DROP TABLE {table};'
				self.cursor.execute(self.string)
				self.conn.commit()
				print("OK champ, whatever you say. It's done!")
			else:
				print("Good. Table not deleted")
		else:
			print("Thought so...")
		#works
	def addColumn(self, table, columnName, dataType):
		self.string = f'ALTER TABLE {table} \nADD {columnName} {dataType};'
		self.cursor.execute(self.string)
		self.conn.commit()
		print(f'Column {columnName} created')
		
	def tableList(self, table):
		try:
			self.string = f'select * from sqlite_master where type = {table}'
			self.cursor.execute(self.string)
			self.conn.commit()
		except:
			print("ERROR occured! The table most likely doesn't exist")
