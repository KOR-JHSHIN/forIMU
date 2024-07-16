#!/usr/bin/env python3

import rospy
import tf
from sensor_msgs.msg import Imu

class IMU:
    def __init__(self):
        rospy.init_node('imu_to_euler', anonymous=True)
        rospy.Subscriber("/imu/data", Imu, self.imu_callback)
        rospy.spin()

    def imu_callback(self, msg): 
        orientation_q = msg.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, yaw) = tf.transformations.euler_from_quaternion(orientation_list)
    
        rospy.loginfo("Roll: %f, Pitch: %f, Yaw: %f", roll, pitch, yaw)

if __name__ == '__main__':
    try:
        IMU()
    except rospy.ROSInterruptException:
        pass
