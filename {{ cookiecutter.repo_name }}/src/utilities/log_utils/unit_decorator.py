# -*- coding:utf-8 -*-
"""
UnitDecorator
-------------------
Decorators to enable an easy debug and partial profiling of the app

.. module:: UnitDecorator
   :synopsis: Decorators to enable an easy debug and partial profiling of the app
.. moduleauthor:: Victor Martinez
"""
from functools import wraps


def function_logger(orig_func):
    """Logs calls to orig_func

    Args:
        orig_func: Function to decorate
    """
    # Logging initialization
    import logging
    logger = logging.getLogger(__name__)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logger.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def function_timer(orig_func):
    """Logs execution time of calls to orig_func

    Args:
        orig_func: Function to decorate
    """
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time()
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper
