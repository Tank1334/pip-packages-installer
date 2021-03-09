
from setuptools import setup, find_packages

setup(
    name = "pip-packages-installer",
    version = "1.0",
    description = "An easy way to install pip packages",
    url = "https://github.com/TridentWolfDev/pip-packages-installer",
    author = "Trident",
    license='MIT',
    install_requires=['tkinter', 'subprocess'],
    packages=find_packages()
)
