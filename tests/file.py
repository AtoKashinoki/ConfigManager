"""
    file tests
"""

from ConfigManager import file

path = "tests/test.config"

if __name__ == '__main__':
    config = file.read(path)
    print(config)
    file.write(config, path)
    ...
