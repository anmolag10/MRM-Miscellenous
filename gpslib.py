import serial
import math
from haversine import haversine, Unit

ser=serial.Serial('/dev/ttyUSB0',4800)
pointB=(13.34786166,74.79216999)
def gps():
    data= ser.readline()
   data= data.decode()
   if data[0:6]=='$GPGGA':
       print('len:',len(data))
       Latitude=data[14:23]
       Longitude=data[26:36]
       Point=(float(Latitude)/100,float(Longitude)/100)
       return Point
point=gps()