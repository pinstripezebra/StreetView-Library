from setuptools import setup, find_packages
  
setup( 
    name='streetviewsampler', 
    version='0.1', 
    description='A python package that randomly samples google streetview images from specified locations', 
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='pinstripezebra', 
    author_email='seelcs12@gmail.com', 
    packages=['StreetViewSampler'], 
    install_requires=[ 
        'os', 
        'pandas',
        'googlemaps',
        'random',
        'requests'
    ], 
) 