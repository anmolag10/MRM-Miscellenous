#! /usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

pub = None
def take_action(regions):
    msg = Twist()
    linear_x = 0
    angular_z = 0

    state_description = ''

    if regions['front'] > 1 and regions['fleft'] > 1 and regions['fright'] > 1:
        state_description = 'case 1 - nothing'
        linear_x = 0.6
        angular_z = 0
    elif regions['front'] < 1 and regions['fleft'] > 1 and regions['fright'] > 1:
        state_description = 'case 2 - front'
        linear_x = 0
        angular_z = -0.3
    elif regions['front'] > 1 and regions['fleft'] > 1 and regions['fright'] < 1:
        state_description = 'case 3 - fright'
        linear_x = 0
        angular_z = -0.3
    elif regions['front'] > 1 and regions['fleft'] < 1 and regions['fright'] > 1:
        state_description = 'case 4 - fleft'
        linear_x = 0
        angular_z = 0.3
    elif regions['front'] < 1 and regions['fleft'] > 1 and regions['fright'] < 1:
        state_description = 'case 5 - front and fright'
        linear_x = 0
        angular_z = -0.3
    elif regions['front'] < 1 and regions['fleft'] < 1 and regions['fright'] > 1:
        state_description = 'case 6 - front and fleft'
        linear_x = 0
        angular_z = 0.3
    elif regions['front'] < 1 and regions['fleft'] < 1 and regions['fright'] < 1:
        state_description = 'case 7 - front and fleft and fright'
        linear_x = 0
        angular_z = -0.3
    elif regions['front'] > 1 and regions['fleft'] < 1 and regions['fright'] < 1:
        state_description = 'case 8 - fleft and fright'
        linear_x = 0
        angular_z = -0.3
    else:
        state_description = 'unknown case'
        rospy.loginfo(regions)

    rospy.loginfo(state_description)
    msg.linear.x = linear_x
    msg.angular.z = angular_z
    pub.publish(msg)
def clbk_laser(msg):
      if str(min(msg.ranges[0:144]))=='nan':
        r1=10
      else:
        r1=(min(msg.ranges[0:144]))
      if str(min(msg.ranges[144:287]))=='nan':
        r2=10
      else:
        r2=(min(msg.ranges[144:287]))
      if str(min(msg.ranges[288:431]))=='nan':
        r3=10
      else:
        r3=(min(msg.ranges[288:431]))
      if str(min(msg.ranges[432:575]))=='nan':
        r4=10
      else:
        r44=(min(msg.ranges[432:575]))
      if str(min(msg.ranges[576:713]))=='nan':
        r5=10
      else:
        r5=(min(msg.ranges[576:713]))   

      regions = {
        'right':  min(r1, 10),
        'fright': min(r2, 10),
        'front':  min(r3, 10),
        'fleft':  min(r4, 10),
        'left':   min(r5, 10), }

      take_action(regions)
	
def main():
    global pub
 
    rospy.init_node('reading_laser')
 
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
 
    sub = rospy.Subscriber('/scan', LaserScan, clbk_laser)
 
    rospy.spin()
 
if __name__ == '__main__':
    main()
