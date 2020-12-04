import matplotlib.pyplot as plt
import random
from scipy.signal import find_peaks as fp
import numpy as np
# 25 samples per second (in algorithm.h)
SAMPLE_FREQ = 25
# taking moving average of 4 samples when calculating HR
# in algorithm.h, "DONOT CHANGE" comment is attached
MA_SIZE = 4
# sampling frequency * 4 (in algorithm.h)
BUFFER_SIZE = 100

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

def smooth_curve_simple(points, sample_size):
    smoothed_points = []
    reads = [0 for _ in range(sample_size)]
    id_reads = 0
    for id, point in enumerate(points):
        reads[id_reads] = point
        id_reads += 1

        if id_reads % sample_size == 0:
            id_reads = 0
            smoothed_points.append((sum(reads)/sample_size, id))

    return smoothed_points

def analisisHR2(hrValues, miliValues, sample_size):
    #smoothed_values = smooth_curve_simple(hrValues, sample_size)
    smoothed_values = [data for data,i in smooth_curve_simple(hrValues, sample_size)]
    peaks = fp(smoothed_values)[0]

    average = []
    for id in range(0, len(peaks)-1,2):
        current = peaks[id+1] * sample_size + sample_size
        previous = peaks[id] * sample_size + sample_size
        average.append(miliValues[current] - miliValues[previous])
        # previous = id*sample_size

    #plt.plot(smoothed_values)
    #plt.scatter(peaks, [smoothed_values[j] for j in peaks], marker='+', c='Red')
    #plt.show()

    valorHR=(60000*len(peaks))/(miliValues[-1] - miliValues[0])
    # valorHR=(60000)/(sum(average)/len(average))
    return valorHR

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 1337))
hrValues = []
miliValues = []
while True:
    try:
        data = s.recv(1024).decode('ascii').rstrip()
        data_split = data.split(";")
        hr = int(data_split[0].split(":")[1])
        milis = int(data_split[1].split(":")[1])

        hrValues.append(hr)
        miliValues.append(milis)
    except:
        continue
    
    if(len(hrValues)==100):
        #print("SPO2:",calc_hr_and_spo2(irValues, redValues))
        #print(irValues)
        #print(redValues)
        bpm = int(analisisHR2(hrValues, miliValues, 1))
        print("HR:", bpm)
        hrValues=hrValues[25:]
        miliValues=miliValues[25:]
        #redValues=redValues[25:]
        #irValues=irValues[25:]


        try:
            cnx = mysql.connector.connect(user='root', password=password, host='127.0.0.1', database='reto')
            cursor = cnx.cursor()

            ox_sat = random.randint(60, 100)
            if ox_sat >= 95:
                state = '"NORMAL"'
            
            elif 91 <= ox_sat <= 94:
                state = '"LEVE"'
            
            elif 86 <= ox_sat <= 90:
                state = '"MODERADO"'
            
            else:
                state = '"SEVERO"'

            query_data = {'user_id': 1, 'date': dateTime(), 'ox_sat': ox_sat, 'bpm': bpm, 'state': state}
            query = (f"INSERT INTO data(user_id, date, ox_sat, bpm, state) values({query_data['user_id']}, {query_data['date']}, {query_data['ox_sat']}, {query_data['bpm']}, {query_data['state']})")
            cursor.execute(query)

            

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