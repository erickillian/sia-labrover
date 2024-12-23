#!/bin/bash
xhost +

docker run -it \
--restart always \
--net=host \
--env="DISPLAY" \
--env="QT_X11_NO_MITSHM=1" \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-v /home/jetson/temp:/root/yahboomcar_ros2_ws/temp \
-v /home/jetson/rosboard:/root/rosboard \
-v /home/jetson/maps:/root/maps \
-v /dev/bus/usb/001/012:/dev/bus/usb/001/012 \
-v /dev/bus/usb/001/013:/dev/bus/usb/001/013 \
--device=/dev/myserial \
--device=/dev/rplidar \
--device=/dev/input \
--device=/dev/astradepth \
--device=/dev/astrauvc \
--device=/dev/video0 \
--device=/dev \
-p 9090:9090 \
-p 8888:8888 \
yahboomtechnology/ros-foxy:4.0.0 /bin/bash

