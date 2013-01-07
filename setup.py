"""
Setup script for PyPi
"""

from distutils.core import setup
setup(name='python-inspector',
    version='0.2.0',
    license='Apache License, Version 2.0',
    description='Track down which Python module and script that called your method. Debug tool.',
    author='Sebastian Dahlgren',
    author_email='sebastian.dahlgren@gmail.com',
    url='http://github.com/sebdah/python-inspector',
    keywords="python inspector inspection tracing tracking",
    py_modules=['inspector'],
    platforms=['Any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)