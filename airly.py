import requests as rq
import json as js
from datetime import datetime
import pytz
import pymysql
import time

#timeout = 3480
#timeout_start = time.time()

#credentials--------------------------------------------------------------------------
def airlyrq (url):
    headers = {
    'Accept' : 'application/json',
    'Accept-Language':'en',
    'apikey': 'IU1E4Ryh7zyMt4glv7LeV72JHkOMoiQ0'
    }
    response = rq.get(url, headers=headers)
    return response
#-------------------------------------------------------------------------------------- 

#Loop repeated every 1 minute over 1 hr   
#while time.time() < timeout_start + timeout:
r = airlyrq('https://airapi.airly.eu/v2/measurements/installation?indexType=AIRLY_CAQI&installationId=2963')
#-------------------------------------------------------------------------------------
#JSON---------------------------------------------------------------------------------
def jprint(obj):
    text = js.dumps(obj, sort_keys=True, indent=4)
    print(text)

#Full sensor reading just for reference when inspecting code
#full_reading = r.json()['current']
#jprint(full_reading)
#-------------------------------------------------------------------------------------

current_reading = r.json()['current']['values']

values = []
for n in current_reading:
    value = n['value']
    values.append(value)
    
#current pollution and weather readings
PM1 = values[0]
PM25 = values[1]
PM10 = values[2]
pressure = values[3]
humidity = values[4]
temperature = values[5]

#outputs['PM1'] = PM1
#outputs['PM25'] = PM25
#outputs['PM10'] = PM10
#outputs['pressure'] = pressure
#outputs['humidity'] = humidity
#outputs['tempereture'] = temperature

#current CAQI
CAQI = r.json()['current']['indexes']
      
caqi = []
for C in CAQI:
    caqi_value = C['value']
    caqi.append(caqi_value)

cq = caqi[0]
#outputs['CAQI'] = cq

#time
tz_GDK = pytz.timezone('Europe/Warsaw')
datetime_GDK = datetime.now(tz_GDK)
#outputs['reading_time'] = str(datetime_GDK)
#print(datetime_GDK, PM1, PM25, PM10, pressure, humidity, temperature, cq)

#Direct query to SQL:
con = pymysql.connect('sql7.freemysqlhosting.net','sql7320329','WuNbHGw5EX','sql7320329')
cur = con.cursor()
cur.execute('INSERT INTO Wojskiego VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(datetime_GDK, PM1, PM25, PM10, pressure, humidity, temperature, cq))
con.commit()
#time delay of 1 minute   
#    time.sleep(60)
