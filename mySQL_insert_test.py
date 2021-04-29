import mysql.connector
from datetime import date, datetime, time

conn = mysql.connector.connect(user='nathan', database='RoofProject', password='eTHrseEb0wot1iC9')
cursor = conn.cursor()

sql = ("""INSERT INTO DHT11
			(timestamp,date,time,temperature,humidity)
			VALUES (%s, %s, %s, %s, %s)""")


now = datetime.now()
dict = {
	now.strftime("%Y-%m-%d %H:%M:%S"),
	now.strftime("%Y-%m-%d"),
	now.strftime("%H:%M:%S"),
	79.5,
	31.5}
	
cursor.execute(sql,(
	now.strftime("%Y-%m-%d %H:%M:%S"),
	now.strftime("%Y-%m-%d"),
	now.strftime("%H:%M:%S"),
	79.5,
	31.5))

conn.commit()
cursor.close()
conn.close()
