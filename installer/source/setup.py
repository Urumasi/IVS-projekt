#!/usr/bin/env python3

# File: setup.py, setup script for the calcchamp package
# Author: OkayChamps, Marek Filip (xfilip46), FIT BUT
# Date: 2020-Apr-29

from setuptools import setup, find_packages

package_name = 'calcchamp'

setup(
    name='calcchamp',
    version='2020.1.0',
    description="Calculator application for champs that are okay.",
    long_description="This calculator was built by blood and sweat amidst\
    great coronavirus crisis of 2020. As of writing this text we are not\
    sure if this project will see the light of day. But anyway, this calc\
    is dedicated to all the OkayChamps out there FeelsOkayMan.",
    keywords="calc calculator okay champ okaychamp",

    author='OkayChamps',
    author_email='wecros@gmail.com',
    url="https://github.com/Urumasi/IVS-projekt",
    project_urls={
        "Assignment": "http://ivs.fit.vutbr.cz/projekt-2_tymova_spoluprace2019-20.html",
    },
    license='GPL-3.0',
    platforms=['any'],

    packages=[package_name],
    entry_points={
        'console_scripts': [f'{package_name} = {package_name}.main:main'],
    },
    data_files=[
        ('share/pixmaps', ['data/OkayChamp.png']),
        ('share/applications', [f'data/{package_name}.desktop'])
    ],

    python_requires='>3.0',
)
