FROM yahboomtechnology/ros-foxy:4.0.0

# Changes the ROBOT Type to be the ROSMASTER R2 in the bashrc file and sources it
# Changes the ROBOT Type to be the ROSMASTER R2 in the bashrc file and sources it
RUN sed -i 's/export ROBOT_TYPE=[^[:space:]]*/export ROBOT_TYPE=r2/' ~/.bashrc \
    && source ~/.bashrc