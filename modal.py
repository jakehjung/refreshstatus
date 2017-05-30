import sqlite3

conn = sqlite3.connect('refresh.db')
c = conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unit REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
	c.execute("INSERT INTO stuffToPlot VALUES(123124, '2016-12-03', 'Python', 5)")
	conn.commit()
	c.close()
	conn.close()

def dynamic_data_entry():
	unix = time.time()
	date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
	keyword = 'Python'
	value = randomrandrange(0,10)
	c.execute("INSERT INTO stsuffToPlot(unix, datestamp, keyword, value) VALUES(?,?,?,?)",
				(unix, date, keyword, value))
	conn.commit()

def read_from_db():
	c.execute('SELECT * FROM stuffToPlot')
	data = c.fetchall()
	print(data)


# create_table()
# data_entry()

read_from_db()
c.close()
conn.close()