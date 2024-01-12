#!/usr/bin/env python
import rospy
from std_msgs.msg import String

yaw_pitch = "{joint_names : ['HeadYaw','HeadPitch'], joint_angles : [0.0,0.5149], speed : 0.055}"
message_type = "JointAnglesWithSpeed"
topic = "/pepper_robot/pose/joint_angles" 

def talker():
    pub = rospy.Publisher(topic, message_type, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    hello_str = "hello world %s" % rospy.get_time()
    pub.publish(yaw_pitch)
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass