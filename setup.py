from setuptools import setup, find_packages
  

setup(
    name="streetviewsampler",
    version="v0.1.1-alpha",
    author="pinstripezebra",
    author_email="seelcs12@gmail.com",
    url="https://github.com/pinstripezebra/StreetView-Library",
    description="A python package that randomly samples google streetview images from specified locations",
    long_description=open('README.rst').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas","googlemaps","requests"],
)