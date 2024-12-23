# sia-labrover
Code for the SIA Lab ROSMASTER R2 setup

## ROS2 Setup for the Yahboom ROSMASTER R2

This device came with ROS1 melodic pre-installed in an environment

The setup instructions from yahboom can be viewed here [http://www.yahboom.net/study/ROSMASTER-R2](http://www.yahboom.net/study/ROSMASTER-R2) section 19.9-1

In the case you want a quick summary you can simply do the following to flash yahbooms ROS2 image:

First unplug the yahboom USB.  Next install a ROS2 image on the usb.

the ROS2 Image can be installed here [ROS2 ROSMASTER R2](https://drive.google.com/drive/folders/1nyf-BhgrBftryZCUAIYJwh2Tsl45R1Ju?usp=drive_link)
 or can be found by scrolling to the bottom of the page on yahbooms [website](http://www.yahboom.net/study/ROSMASTER-R2) and use the link there (System file for NANO-ROS2)

Next use SDFormatter to format the flash drive.  Then use Win32 or an image installer such as balenaEtcher to upload the image onto the drive.

Once the image is installed add it to the yahboom car and power on.  
There is an app startup that runs, first disable this.  

Open Ubuntu system applications, search Startup Applications, remove the check mark in front of start_rosmaster_app as shown in the following figure to close the large program permanently.

Next run the docker container on the image to start ROS2.

```
~/run_docker.sh
```

I was running into issues where the /dev/astradepth device could not be found.  If you run into this issue unplug and replug the camera and this device should show up.  To make sure run 

```sh
ls /dev | grep astra
```

and you should see 

```
astradepth
astrauvc
```
show up

you can then run 

```
~/run_docker.sh
```


This will run a docker image inside linux that is running ROS2

Next close out of this docker image, as this is just to verify that docker is working on the device.

# ROS2 Custom Docker Setup

There are some issues with things running inside this docker container so modifications needed to be made.  I made a custom Dockerfile which runs these modifications as well as a custom volume inside the docker container to store any custom code which we might want to run.

now clone this repo onto the jetson

```
cd ~
git clone https://github.com/erickillian/sia-labrover.git
cd sia-labrover
docker build -t my-custom-ros-foxy .
```

This will build a new docker image called my-custom-ros-foxy that makes some updates

To start the modified docker container run
```
~/sia-labrover/run_modified_docker.sh
```

To stop the modified docker container run
```
~/sia-labrover/stop_modified_docker.sh
```

which will run the revised ROS2 image as a daemon.

To connect to a terminal inside the ROS2 docker image run 
```
docker exec -it my-custom-ros-foxy /bin/bash
```

Or you can just run 
```
~/sia-labrover/enter_docker.sh
```

Next in an attempt to see things working you can run yahbooms [Ackman Driver](./yahboomcar_ros2_ws/yahboomcar_ws/src/yahboomcar_bringup/yahboomcar_bringup/Ackman_driver_R2.py) 


First enter the docker container and then run
```
ros2 run yahboomcar_bringup Ackman_driver_R2
```

To use [keyboard control](./yahboomcar_ros2_ws/yahboomcar_ws/src/yahboomcar_ctrl/yahboomcar_ctrl/yahboom_keyboard.py) then run 
```
ros2 run yahboomcar_ctrl yahboom_keyboard
```

For info on how the keyboard controls work see [ROSMASTER site](http://www.yahboom.net/study/ROSMASTER-R2) section 22.3.2 Keyboard control for more info.


# Yahboom ROSMASTER R2 Hardware control

It seems that all hardware control including turning on motors, LED lightbar, and servos go through the Rosmaster_lib python package and the code can be found [here](yahboomcar_ros2_ws/software/py_install_V3.3.1/Rosmaster_Lib/Rosmaster_Lib.py)

To test this package some testing scripts were made [here](./sia-lab-workspace/hardware-tests/)