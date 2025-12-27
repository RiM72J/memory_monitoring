#!/bin/bash
# SPDX-FileCopyrightText: 2025 RiMC7
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws

colcon build --packages-select memory_monitoring
source install/setup.bash

timeout 15 ros2 launch memory_monitoring memory_monitoring.launch.py > /tmp/memory_monitoring.log

cat /tmp/memory_monitoring.log | grep 'Normal:'
