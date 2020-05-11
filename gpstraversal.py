import gpslib
import bearinglib
import headinglib
from haversine import haversine, Unit
pointB=(13.34786166,74.79216999)
df=haversine(gpslib.gps(),pointB)
while True:
    d=haversine(gpslib.gps(),pointB)
    val=bearinglib.bearing(pointB)-headinglib.heading()
    if(val>0):
        if(abs(val)>180):
            print('Move clockwise')
        elif(abs(val<180)):
            print('Move anitclockwise')
        elif(val in range(0,5)):
            print('Aligned to the point')
            if(d>df):
                print('Move Backward')
            elif(df>d):
                print('Move Forward')        
    else:
        if(abs(val)<180):
            print('Move clockwise')
        elif(val>180):
            print('Move anitclockwise')
        elif(val in range(-5,5)):
            print('Aligned to the point')
            print('Aligned to the point')
            if(d>df):
                print('Move Backward')
            elif(df>d):
                print('Move Forward')    
 