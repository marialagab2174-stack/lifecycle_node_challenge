from setuptools import find_packages, setup

package_name = 'lifecycle_node_challenge'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Maria Lagab',
    maintainer_email='marialagab2174@gmail.com',
    description='Challenge ROS 2 - Lifecycle Node Management',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'lc_node = lifecycle_node_challenge.lifecycle_node:main'
        ],
    },
)
