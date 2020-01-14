## ROBOTIC INTEGRATION

### Exercise 2.1

1- Create the <PROJECT> package with the following lines:


```sh
~/Desktop/Master Robotica/integracion_robotica$ catkin_create_pkg project_uvic_ac std_msgs rospy roscpp
```

2- Customize the “package.xml” file:

```sh 
~/catkin_ws/src$ cd rosruncd project_uvic_ac

~/catkin_ws/src/project_uvic_ac$ gedit package.xml 
```

```sh 
<?xml version="1.0"?>
<package format="2">
  <name>project_uvic_ac</name>
  <version>0.0.0</version>
  <description>The project_uvic_ac package</description>

  <!-- One maintainer tag required, multiple allowed, one person per tag -->
  <!-- Example:  -->
  <!-- <maintainer email="dlvmaster.robotics@gmail.com ">Damaris LV</maintainer> -->
  <maintainer email="gengiro@todo.todo">gengiro</maintainer>
```

3- Create the repository “config” and “launch” so we can create inside the files “project_param.launch ” and “param.yalm”:

```sh 
~/catkin_ws/src/project_uvic_ac$ mkdir config

~/catkin_ws/src/project_uvic_ac/config$ cat >param.yalm


~/catkin_ws/src/project_uvic_ac$ mkdir  launch

~/catkin_ws/src/project_uvic_ac/launch$ cat >project_param.launch 
```


4- Configure the launch file so when executing it we will get:

- “year” parameter loaded from “param.yaml” file.
- “rviz” node, so we can execute also “rviz”.
- Including the launch file from the package “usb_cam”, so we turn the computer camera on.


```sh 
<launch> 

	<param name="yaml_cfg_file" value="$(find project_uvic_ac)/config/param.yalm" />

	<node type="rviz" name="rviz" pkg="rviz" />

	<include file="$(find usb_cam)/launch/usb_cam-test.launch"/>
	
</launch>
```

To run all of this, we should type:


~/catkin_ws/src$ roslaunch project_uvic_ac project_param.launch 
```

5- The arguments for “usb_cam_test.launch” are:

~video_device (string, default: "/dev/video0") 
    • The device the camera is on. 
~image_width (integer, default: 640) 
    • Image width 
~image_height (integer, default: 480) 
    • Image height 
~pixel_format (string, default: "mjpeg") 
    • Possible values are mjpeg, yuyv, uyvy 
~io_method (string, default: "mmap") 
    • Possible values are mmap, read, userptr 
~camera_frame_id (string, default: "head_camera") 
    • The camera's tf frame 
~framerate (integer, default: 30) 
    • The required framerate 
~contrast (integer, default: 32) 
    • Contrast of video image (0-255) 
~brightness (integer, default: 32) 
    • Brightness of video image (0-255) 
~saturation (integer, default: 32) 
    • Saturation of video image (0-255) 
~sharpness (integer, default: 22) 
    • Sharpness of video image (0-255) 
~autofocus (boolean, default: false) 
    • Enable camera's autofocus 
~focus (integer, default: 51) 
    • If autofocus is disabled, the focus of the camera (0=at infinity) 
~camera_info_url (string, default: ) 
    • An url to the camera calibration file that will be read by the CameraInfoManager class 
~camera_name (string, default: head_camera) 
    • The camera name. This must match the name in the camera calibration 
