#!/usr/bin/env python
import rospy
from sensor_msgs.msg import NavSatFix,Imu
from tf.transformations import euler_from_quaternion
import math as m
#import haversine
pointf=(49.9001891682,8.90004687712)
def callback1(data):
    lat=data.latitude
    lon=data.longitude
    print('long lat',lon,lat)
def callback2(data2):
   quaternion=(data2.orientation.x,data2.orientation.y,data2.orientation.z,data2.orientation.w)
   euler=euler_from_quaternion(quaternion)
   
   
   

def listener():
        try:
            rospy.init_node('gps','imu', anonymous=True)
            
            rospy.Subscriber("fix", NavSatFix, callback1)
            rospy.Subscriber("imu", Imu, callback2)

            rospy.spin()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    
    listener()
    print(euler)
    

