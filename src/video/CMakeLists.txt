cmake_minimum_required(VERSION 3.0.2)
project(video)


find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  image_transport
  roscpp
  rospy
  sensor_msgs
  std_msgs
)

find_package(OpenCV)
include_directories(${OpenCV_INCLUDE_DIRS})

catkin_package(
  CATKIN_DEPENDS cv_bridge image_transport roscpp rospy sensor_msgs std_msgs
)


include_directories(${catkin_INCLUDE_DIRS})

add_executable(video_publisher src/video_publisher.cpp)
target_link_libraries(video_publisher ${catkin_LIBRARIES})
target_link_libraries(video_publisher ${OpenCV_LIBRARIES})
