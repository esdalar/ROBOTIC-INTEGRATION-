#! /usr/bin/env python

import rospy
from std_msgs.msg import String

def year():
	pub = rospy.Publisher('topic', String,queue_size=10)
	rospy.init_node('year',anonymous = True)
	print "Nodo creado con exito"
	rate = rospy.Rate(10) #frecuencia de publicacion 10 veces por segundo
	while not rospy.is_shutdown():
			year_data = "Year 2019 %s" % rospy.get_time()
			pub.publish(year_data)
			print year_data
			rate.sleep()

if __name__ == '__main__':
	try:
		year()
	except rospy.ROSInterruptException:
		pass
