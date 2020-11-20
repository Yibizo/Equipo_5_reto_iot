password = '@Bril152000'
import mysql.connector
import random

def dateTime():
      month = random.randint(1, 12)
      if month == 2:
        day = random.randint(1, 29)
      elif month in [1,3,5,7,8,10,12]:
        day = random.randint(1,31)
      else:
        day = random.randint(1,30)

      date = f'"2020-{month}-{day} {random.randint(0, 23)}:{random.randint(0,59)}:{random.randint(0,59)}"'
      return date


try:
    cnx = mysql.connector.connect(user='root', password=password, host='127.0.0.1', database='reto')
    cursor = cnx.cursor()

    for _ in range(4999):
      ox_sat = random.randint(60, 100)
      if ox_sat >= 95:
        state = '"NORMAL"'
      
      elif 91 <= ox_sat <= 94:
        state = '"LEVE"'
      
      elif 86 <= ox_sat <= 90:
        state = '"MODERADO"'
      
      else:
        state = '"SEVERO"'

      query_data = {'user_id': 1, 'date': dateTime(), 'ox_sat': ox_sat, 'bpm': random.randint(80, 120), 'state': state}
      query = (f"INSERT INTO data(user_id, date, ox_sat, bpm, state) values({query_data['user_id']}, {query_data['date']}, {query_data['ox_sat']}, {query_data['bpm']}, {query_data['state']})")
      cursor.execute(query, query_data)

    

    cnx.commit()
except mysql.connector.Error as err:

  if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
    
finally:
  cnx.close()