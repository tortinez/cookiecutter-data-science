# -*- coding:utf-8 -*-
"""
Config
-------------------
Configuration variables for the {{cookiecutter.project_name}} project

.. module:: Config
   :synopsis: Configurations for the project
.. moduleauthor:: Victor Martinez
"""

import os

from dotenv import load_dotenv, find_dotenv

BASEDIR = os.path.join(os.path.dirname(__file__), '..')

# load dotenv in the base root
dotenv_path = os.path.join(BASEDIR, '.env')
load_dotenv(find_dotenv())


# Configuration Variables
DEBUG = (os.environ.get('DEBUG') or False)
