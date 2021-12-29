from os import read
from setuptools import setup

with open("README.md","r",encoding="utf-8") as readme_file:
    long_description=readme_file.read()

setup(
    name="linuxstore",
    version="1.0.0",
    description="A app store for linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Arjun",
    author_email="jakkipally@gmail.com",
    license="MIT",
    packages=['linuxstore'],
    package_dir={'linuxstore':'linuxstore/'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Enviroment :: Console",
        "Operating System :: POSIX :: Linux"
    ],
    entry_points={
        'console_scripts':['linuxstore=linuxstore.linuxstore:main']
    },
    data_files=[
        ('share/applications/',['linuxstore.desktop'])
    ],
    keywords="linuxstore",
    python_requires=">=3.6"
)