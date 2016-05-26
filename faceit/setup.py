# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='faceit',
    packages=find_packages(exclude=['tests*']),
    version='0.0.1',
    author=u'Ben Lambert',
    author_email='ben.lambert@cloudacademy.com',
    url='https://github.com/whelmed/devops_ci_demo.git',
    license='BSD licence',
    description='A fake app for a demo',
    long_description="This is really just a demo.",
    zip_safe=False,

    install_requires=[
      "django==1.9",
      "name-tools==0.1.3",
    ],
    classifiers=[
        "Private :: Do Not Upload"
    ],
)
