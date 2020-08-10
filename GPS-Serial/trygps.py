import serial
import math
from haversine import haversine, Unit
import smbus	
from time import sleep 
Register_A     = 0             
Register_B     = 0x01          
Register_mode  = 0x02           
X_axis_H    = 0x03              
Z_axis_H    = 0x05              
Y_axis_H    = 0x07              
         
pi= 3.14159265359
ser=serial.Serial('/dev/ttyUSB0',4800)
pointB=(13.34786166,74.79216999)
def heading():
      def Magnetometer_Init():
        #write to Configuration Register A
        bus.write_byte_data(Device_Address, Register_A, 0x70)

        #Write to Configuration Register B for gain
        bus.write_byte_data(Device_Address, Register_B, 0xa0)

        #Write to mode Register for selecting mode
        bus.write_byte_data(Device_Address, Register_mode, 0)

      def read_raw_data(addr):

            #Read raw 16-bit value
            high = bus.read_byte_data(Device_Address, addr)
            low = bus.read_byte_data(Device_Address, addr+1)

            #concatenate higher and lower value
            value = ((high << 8) | low)

            #to get signed value from module
            if(value > 32768):
                value = value - 65536
            return value
  
      
      bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
      Device_Address = 0x1e   # HMC5883L magnetometer device address

      Magnetometer_Init()     # initialize HMC5883L magnetometer
      x = read_raw_data(X_axis_H)
      z = read_raw_data(Z_axis_H)
      y = read_raw_data(Y_axis_H)
      heading = math.atan2(y, x)
      if(heading > 2*pi):
          heading = heading - 2*pi
      if(heading < 0):
         heading= heading + 2*pi
         heading_angle = int(heading * 180/pi)
      return (heading_angle-88)
    
def bear(pointA,pointB):
    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")
    lat1 = math.radians(pointA[0])
    lat2 = math.radians(pointB[0])
    diffLong = math.radians(pointB[1] - pointA[1])
    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1)*math.sin(lat2)-(math.sin(lat1)* math.cos(lat2) * math.cos(diffLong))
    initial_bearing = math.atan2(x, y)
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360
    return compass_bearing

while True:
   data= ser.readline()
   data= data.decode()
   if data[0:6]=='$GPGGA':
       Latitude=data[14:23]
       Longitude=data[26:36]
       try:
        PointA=(float(Latitude),float(Longitude)))
        bearing=bear(PointA,pointB)
        head=heading()
        print(str(bearing-head)+'/t'+str(haversine(PointA,pointB)))
       except:
         pass





