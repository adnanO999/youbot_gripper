cmake_minimum_required(VERSION 2.8.3)

project(total_assembly_gripper)



find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

catkin_package()

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

catkin_install_python(PROGRAMS
  scripts/initial_config.py
  scripts/set_desired_position.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)