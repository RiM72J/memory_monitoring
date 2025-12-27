from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='memory_monitoring',
            executable='talker',
            name='memory_talker'
        ),
        Node(
            package='memory_monitoring',
            executable='listener',
            name='memory_listener'
        )
    ])
