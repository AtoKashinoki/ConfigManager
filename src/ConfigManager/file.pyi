
# import Config class
from .config import Config


# variables
config_file_format: str


# functions

def write(
        config: dict[str, str | int | float] | Config,
        path: str,
        encoding: str = "UTF-8",
) -> None: ...

def read(path: str, encoding: str = "UTF-8") -> dict: ...
