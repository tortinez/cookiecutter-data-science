# -*- coding:utf-8 -*-
"""
Run
-------------------
Entrypoint to the application

.. module:: Run
   :synopsis: Entrypoint to the application
.. moduleauthor:: Victor Martinez
"""
# Logging initialization
import logging
from utilities.log_utils import logger_init
logger = logging.getLogger(__name__)

import config

if __name__ == '__main__':
    logger.info('Application Running')
