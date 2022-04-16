"""
This file defines the map for models.
"""


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ModelMap(dict, metaclass=Singleton):
    """
    This class is a Singleton held dictionary to keep track of models in the program.
    """
    def __init__(self) -> None:
        """
        The constructor for the ModelMap class.
        """
        super().__init__({})

    def add_model(self, model) -> None:
        """
        Adds a model to the map.

        :param model: the model to be added
        :return: None
        """
        self[model.name] = model
