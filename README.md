# youbot_gripper
ROS package for a customized youbot gripper

* Gripper URDF
* Rviz visualisation
  ''' shell
  cd <package_dir>
  catkin_make
  source devel/setup.bash
  roslaunch total_assembly_gripper dispaly.rviz
  '''
* set_desired_position.py script that subscribes to /joint_states and move the gripper
''' console
chmod +x <script_dir>
rosrun total_assembly_gripper set_desired_position.py
'''
* arduino Serial communication with ROS
