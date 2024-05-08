"""
    Config Manager

This module introduces config management classes and functions.

"""

# import sys
import sys


__self_name__ = "ConfigManager"


if not __name__ == __self_name__:
    print("execute failed")
    sys.exit()


""" Import self """


try:
    from .config import Config
    ...
except ImportError as message:
    Config = ImportError(message)
    ...


try:
    from . import file
    ...
except ImportError as message:
    file = ImportError(message)
    ...


print("Initialize {}.".format(__self_name__))
