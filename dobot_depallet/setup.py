from setuptools import find_packages, setup
import glob, os
package_name = 'dobot_depallet'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/model', glob.glob(os.path.join('model', '*.pth'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mkh',
    maintainer_email='kyung133851@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'find_roi=dobot_depallet.find_roi:main',
            'find_box=dobot_depallet.find_box:main',
            'depllet=dobot_depallet.depllet:main'
        ],
    },
)
