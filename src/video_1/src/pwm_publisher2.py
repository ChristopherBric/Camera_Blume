#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Joy


joy_pos1 = 0
joy_pos2 = 0
joy_pos3 = 0
joy_pos4 = 0

def callback(msg):
	global joy_pos1
	global joy_pos2
	global joy_pos3
	global joy_pos4

	joy_pos1 = msg.axes[1]
	joy_pos2 = msg.axes[0]
	joy_pos3 = msg.axes[4]
	joy_pos4 = msg.axes[3]
	#print(joy_pos)

def main():

	rospy.init_node("ds4_publisher")
	rospy.Subscriber("/joy",Joy,callback)
	pub = rospy.Publisher('/thrust_states',JointState,queue_size=1000)

	jnames = ['T1','T2','T3','T4','T5','T6','T7','T8']
	#q = [93,93,93,93,93,93,93,93]
	q = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ]

	jstate = JointState()

	jstate.header.stamp = rospy.Time.now()
	jstate.name = jnames
	jstate.position = q

	rate = rospy.Rate(20)

	while not rospy.is_shutdown():

		jstate.header.stamp = rospy.Time.now()

		q[0] = round(40*joy_pos4  -40*joy_pos3)
		q[1] = round(-40*joy_pos4 -40*joy_pos3)
		q[2] = round(-40*joy_pos1)
		q[3] = round(-40*joy_pos1)

		jstate.position = q
		pub.publish(jstate)

		rate.sleep()
if __name__=='__main__':
	main()

