
from ConfigManager import config

if __name__ == '__main__':
    config1 = config.Config("./tests/test.config")
    config1.write().read()
    config2 = config1.copy("./tests/test2.config")
    with config2 as config:
        config["add"] = 3
        ...
    ...
