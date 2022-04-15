

class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ModelMap(dict, metaclass=Singleton):

    def __init__(self) -> None:
        super().__init__({})

    def add_model(self, model) -> None:
        self[model.name] = model
