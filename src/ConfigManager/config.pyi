
# Config class


class Config(dict):

    file_path: str
    encoding: str

    from . import file
    __file: file = file

    def __init__(
            self,
            path: str,
            encoding: str = "UTF-8",
    ): ...

    def read(self):
        return self

    def write(self):
        return self

    def copy(self, path: str) -> Config: ...

    ...
