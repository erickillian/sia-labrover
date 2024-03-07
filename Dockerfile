FROM yahboomtechnology/ros-foxy:4.0.0

# Changes the ROBOT Type to be the ROSMASTER R2 in the bashrc file and sources it
# RUN sed -i 's/export ROBOT_TYPE=[^[:space:]]*/export ROBOT_TYPE=r2/' ~/.bashrc
COPY yahboomcar_ros2_ws/Rosmaster/RobotType/bashrc_files/R2_a1.bashrc /root/.bashrc
# RUN source ~/.bashrc
