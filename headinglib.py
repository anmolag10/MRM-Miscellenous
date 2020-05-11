import smbus	
from time import sleep 
import math
Register_A     = 0             
Register_B     = 0x01          
Register_mode  = 0x02           
X_axis_H    = 0x03              
Z_axis_H    = 0x05              
Y_axis_H    = 0x07              
declination = -0.00669         
pi          = 3.14159265359     
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
    heading = math.atan2(y, x) + declination       
    if(heading > 2*pi):
        heading = heading - 2*pi
    if(heading < 0):
    heading = heading + 2*pi
    heading_angle = int(heading * 180/pi)
    return heading_angle