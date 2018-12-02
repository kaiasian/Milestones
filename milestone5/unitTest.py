#!/usr/bin/env python	
import sqlite3	
import os	
import time	
import glob	
 #csci3308 milestone 4 script	
#This script is used on the raspberry pi 3 B+ to get temperature data and store it	
#in a sql database that is also on the raspberry pi 3 B+.	
#The name of the sensor device file: #28-00000a3cdc2c	
#Device File Path:  /sys/bus/w1/devices/28-00000a3cdc2c/w1_slave	
 #Global Variables	
#sampling frequency for sensor:	
sample = (5*60)-1	
#database object to store at sql path: sensor.db	
myDatabase = 'sensorlog.db'	
#devive file	
#device_file = '28-00000a3cdc2c'	
#Function to measure temperature from device file for DS18B20 sensor	
 #storing the sensor data in the sql databse or any database	
def storage(temp):	
     #connect class is used to connect to sql database also used for socket programming	
    db_connect = sqlite3.connect(myDatabase)	
    #cursor class allows Python to execute PostgreSQL command in database session	
    db_cursor = db_connect.cursor()	
    db_cursor.execute("INSERT INTO temps values(datetime('now'), (?))", (temp,))	
     #commit changes to database SQL	
    db_connect.commit()	
    #terminate connection to database SQL	
    db_connect.close()	
 #display database	
#Unit Test 1: Test to see if there is valid data in the database, and if not then output an error
def display():	
     db_connect = sqlite3.connect(myDatabase)	
    db_cursor = db_connect.cursor()	
     #iterate through contents of db	
    for row in db_cursor.execute("SELECT * FROM temps"):	
        if row == 'None': 	
      # print str(row[0])+""+str(row[1])	
            print("None is read")	
	    #add code to cause an error in the code
        else:	
            print row	
    	
    db_connect.close()	
 def getData(devicefile):	
     try:	
        data_object = open(devicefile, 'r')	
        lines = data_object.readlines()	
        data_object.close()	
    except:	
        return None	
     #Display status	
    status = lines[0][-4:-1]	
     #if sensor data reading is succesful	
    if status == "YES":	
        store_data = lines[1][-6:-1]	
        data_value = float(store_data)/1000	
        print data_value	
        return data_value	
    else:	
        print "Error: Device has encountered an issue "	
        return None	
 #main	
def main():	
     #enable kernel modules for sensor device and gpio pins 	
  #   os.system('sudo modprobe w1-gpio')	
  #  os.system('sudo modprobe w1-therm')	
    #search for sensor device path (cd /sys/bus/w1/devices/28*) to device address	
   # devicelist = glob.glob('/sys/bus/w1/devices/28*')	
    devicelist = glob.glob('unitTest.txt')	
    if devicelist == '':	
        print("now value to read")	
        return None	
    else:	
        #append /w1_slave to device file path	
       # w1_devicefile = devicelist[0] + '/w1_slave'	
        unitTest_file = devicelist	
    #while true	
    #call getData function from devicefile	
    temperature = getData(unitTest_file)	
    if temperature != None:	
        print "temperature = "+str(temperature)	
    else:	
        temperature = getData(unitTest_file)	
        print "temperature="+str(temperature)	
     #store the data	
    storage(temperature)	
     #show database	
    display()	
    #time.sleep(meausre)	
 if __name__=="__main__":	
     main()
