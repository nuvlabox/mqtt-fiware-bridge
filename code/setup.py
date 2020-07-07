from setuptools import setup, find_packages


setup(
    name='mqtt-fiware-bridge',
    version='0.0.1',
    packages=find_packages(),
    description='Reads from an MQTT broker, validates the message schema against FIWARE, and forwards the message',
    author='Cristovao Cordeiro',
    author_email='cristovao.cordeiro@sixsq.com',
    url='https://github.com/nuvlabox/mqtt-fiware-bridge',
    install_requires=[
        'paho-mqtt',
        'fastjsonschema'
    ],
    include_package_data=True
)