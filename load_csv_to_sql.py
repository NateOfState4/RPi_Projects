import mysql.connector
from datetime import date, datetime, time
import pandas as pd

header_list = ['Datetime', 
				'Needs_Water',
				'Avg_Moisture',
				'Soil_Sensor_1',
				'Soil_Sensor_2',
				'Soil_Sensor_3',
				'Temp_Sensor_1',
				'Hum_Sensor_1',
				'Temp_Sensor_2',
				'Hum_Sensor_2']
data = pd.read_csv('/home/nathan/Roof_Production/test_log.csv',
					names=header_list,
					skiprows=1)
data = data.drop(columns=['Needs_Water','Avg_Moisture'])
data.head()

conn = mysql.connector.connect(user='nathan', database='RoofProject', password='eTHrseEb0wot1iC9')
cursor = conn.cursor()

sql = ("""INSERT INTO SENSORS
			(timestamp,
			temperature1,temperature2,
			humidity1,humidity2,
			moisture1,moisture2,moisture3)
			VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""")
for i, row in data.iterrows():
	cursor.execute(sql,tuple(row))
	conn.commit()
	
cursor.close()
conn.close()
