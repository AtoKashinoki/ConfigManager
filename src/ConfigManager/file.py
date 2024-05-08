"""
    ConfigManager.file

This file contain functions to write and read.
"""

# import config class
from .main import Config


""" setting """


config_file_format: str = "{}: {}\n"


""" write """


def write(
        config: dict[str, str | int | float] | Config,
        path: str,
        encoding: str = "UTF-8",
) -> None:
    """
        Write config data in file.
    :param config: dictionary or Config class of config data.
    :param path: file path to write data.
    :param encoding: text code.
    """

    # encode config file format
    config_text: str = ""
    for key, value in config.items():
        config_text += config_file_format.format(
            key,
            value if not type(value) is str else f'"{value}"'
        )
        continue

    # write in file
    with open(file=path, mode="w", encoding=encoding) as file:
        file.write(config_text)
        ...

    return


""" read """


def read(path: str, encoding: str = "UTF-8") -> dict:
    """
        Read and return config data from file.
    :param path: file path to read.
    :param encoding: text code.
    :return: dictionary format config datas.
    """
    # decode file data
    with open(path, mode="r", encoding=encoding) as file:
        config_dict: dict[str, str | int | float] = {
            key:
                str(value[1:-1]) if value[0] == '"' and value[-1] == '"' else
                float(value) if "." in value else
                int(value)
            for line in file.readlines()
            for key, value in [
                line
                .replace(" ", "")
                .replace("\n", "")
                .split(":")
            ]
        }
    return config_dict

