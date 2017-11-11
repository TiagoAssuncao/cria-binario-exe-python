# -*- coding: utf-8 -*-
from setuptools import find_packages
from cx_Freeze import setup, Executable
from configparser import ConfigParser

configuration = ConfigParser()
configuration.read("config.ini")

version = configuration.get('Info', 'Version')
arquivo = configuration.get('Info', 'Script')
description = configuration.get('Info', 'Description')
name = configuration.get('Info', 'Autor')

base = None
executables = [Executable(arquivo, base=base)]

packages=find_packages()
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = name,
    options = options,
    version = version,
    description = description,
    executables = executables
)
