
# !/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
import SillyServer

setup(
    name="SillyServer",
    version=SillyServer.__VERSION__,
    author=SillyServer.__AUTHOR__,
    url=SillyServer.__URL__,
    license=SillyServer.__LICENSE__,
    packages=find_packages(),
    description="A web framework that is silly",
    keywords="silly server",
    test_suite="nose.collector"
)
