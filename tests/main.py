
from ConfigManager import main

if __name__ == '__main__':
    config1 = main.Config("./test.config")
    config1.write().read()
    config2 = config1.copy("./test2.config")
    with config2 as config:
        config["add"] = 3
        ...
    ...
