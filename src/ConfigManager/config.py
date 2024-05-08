"""
    ConfigManager.main

This file contain Config class.
That manage config file and config datas.

"""

# import descriptors
from Descriptors import (
    DataType,
)


""" Config class """


class Config(dict):
    """
        Config dictionary.

    This class inherited dictionary type.
    """

    # variables
    file_path: str = DataType(str)
    encoding: str = DataType(str)

    # constants

    def __init__(
            self,
            path: str,
            encoding: str = "UTF-8"
    ):
        """
            Initialize settings and self.
        :param path: file path to using.
        :param encoding: text code.
        """
        # initialize setting variables
        self.file_path = path
        self.encoding = encoding

        # import ConfigManager.file
        from . import file
        self.__file: file = file

        # initialize dictionary of self
        dict.__init__(self)

        # read file
        try:
            self.read()
            ...
        except FileNotFoundError:
            self.__file.write(self, self.file_path, self.encoding)
            ...

        return

    def read(self):
        """
            Read and register data in file.
        :return: Self
        """
        self.clear()
        [
            self.__setitem__(*item)
            for item in self.__file.read(
                self.file_path, self.encoding
            ).items()
        ]
        return self

    def write(self):
        """
            Write data in file.
        :return: Self
        """
        self.__file.write(self, self.file_path, self.encoding)
        return self

    def copy(self, path: str):
        """
            Copy config file.
        :param path: file path to copy.
        :return: Config << file_path = path
        """
        config_copy: Config = Config(self.file_path, self.encoding)
        config_copy.file_path = path
        config_copy.write()
        return config_copy

    def __enter__(self):
        self.read()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.write()
        return

    ...
