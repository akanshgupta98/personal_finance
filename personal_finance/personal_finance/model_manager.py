from abc import ABC, abstractmethod


class ModelManager(ABC):
    """
    Abstract base class for managing models.

    This class provides a structure for handling different models.
    Subclasses should implement the `get_model` method to return the specific model they manage.

    Attributes:
        model: The model managed by the class. Should be set in subclasses.
    """

    def __init__(self):
        """
        Initializes the ModelManager with a default value of None for the model attribute.
        """
        self.model = None

    @abstractmethod
    def get_model(self):
        """
        Abstract method to get the model managed by the class.

        Returns:
            The model managed by the class. This method should be overridden in subclasses.
        """
        return self.model
