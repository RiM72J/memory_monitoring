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
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rimu2434',
    maintainer_email='iinu04835@gmail.com',
    description='A package to monitor system memory usage and publish alerts.',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = memory_monitoring.memory_talker:main',
            'listener = memory_monitoring.memory_listener:main',
        ],
    },
)
