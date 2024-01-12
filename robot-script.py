# TLDR: Python script using ROS to read a topic and display messages.

import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import numpy as np
import cv2
from green_dot import green_dot_finder

topic_camera_up = "/pepper_robot/camera/front/image_raw"
topic_head = "/pepper_robot/pose/joint_angles" 
joint_message_type = "naoqi_bridge_msgs/JointAnglesWithSpeed"

received_message = False

pub = rospy.Publisher('/status', joint_message_type, queue_size=1000) 

def message_callback(msg):
    global received_message
    if not received_message:
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
        image_array = np.array(cv_image)
        cv2.imwrite('image_data.jpg', cv_image)
        if green_dot_finder('image_data.jpg'):
            print("box detected")
        else:
            print("no box, clear to go")
        received_message = True
        rospy.signal_shutdown("Message received, shutting down.")

def listener():
    rospy.init_node('message_listener', anonymous=True)
    rospy.Subscriber(topic_camera_up, Image, message_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
