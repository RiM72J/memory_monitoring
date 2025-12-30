# SPDX-FileCopyrightText: 2025 Ryomu Inukai
# SPDX-License-Identifier: BSD-3-Clause


from glob import glob
import os

from setuptools import find_packages, setup

package_name = 'memory_monitoring'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['LICENSE']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ryomu Inukai',
    maintainer_email='iinu04835@gmail.com',
    description='ROS 2 package for memory monitoring',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = memory_monitoring.memory_talker:main',
            'listener = memory_monitoring.memory_listener:main',
        ],
    },
)
