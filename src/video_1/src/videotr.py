#!/usr/bin/env python
import numpy as np
import rospy
import cv2
import sys
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

br=CvBridge()
cap = cv2.VideoCapture(0)
def talker():
    pub=rospy.Publisher('video_topic',Image,queue_size=10)
    rospy.init_node('videotr',anonymous=True)
    while not rospy.is_shutdown():
        ret,img = cap.read()
        pub.publish(br.cv2_to_imgmsg(img,'bgr8'))
        cv2.waitKey(1)
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptExeption:
        pass

