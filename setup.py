#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Flask-Quik
--------------

Flask quik integration.

Links
`````

* `development version
*   <http://github.com/avelino/flask-quik>`_
"""
from setuptools import setup


setup(
    name='Flask-Quik',
    version='0.1.1',
    url='http://github.com/avelino/Flask-Quik',
    license='MIT',
    author='Thiago Avelino',
    author_email='thiago@avelino.xxx',
    description='Quik for Flask',
    long_description=__doc__,
    zip_safe=False,
    platforms='any',
    py_modules=['flask_quik'],
    install_requires=['Flask', 'quik'],
    tests_require=['Flask-Testing'],
    test_suite="tests.test_quik.suite",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
