#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Ryomu Inukai
# SPDX-License-Identifier: BSD-3-Clause

ng () {
      echo ${1}行目が違うよ
      res=1
}

res=0

source /opt/ros/jazzy/setup.bash
cd $HOME/ros2_ws

colcon build --packages-select memory_monitoring || ng "$LINENO"
source $HOME/ros2_ws/install/setup.bash

timeout 15 ros2 launch memory_monitoring memory_monitoring.launch.py > /tmp/memory_monitoring.log 2>&1 || true

count=$(grep -c "Normal:" /tmp/memory_monitoring.log)

[ "$count" -ge 1 ] || ng "$LINENO"

[ "$res" = 0 ] && echo OK

exit $res
