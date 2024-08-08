# youbot_gripper
ROS package for a customized youbot gripper
* Gripper URDF
* Rviz visualisation
* Arduino Serial communication with ROS
  
# Setup and Run Instructions

## Build the ROS Package

Navigate to your package directory and build the package:
```shell
cd <package_dir>
catkin_make
source devel/setup.bash
  ```
 
 ## Launch Rviz
```shell 
  roslaunch total_assembly_gripper dispaly.rviz
  ```
## Move the Gripper

set_desired_position.py script that subscribes to /joint_states and move the gripper
```shell 
chmod +x <script_dir>
rosrun total_assembly_gripper set_desired_position.py
```

