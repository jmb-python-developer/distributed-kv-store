from abc import ABC, abstractmethod
from typing import Dict, Any, Union

class SerializerInterface(ABC):
    """
    Abstract interface for serializing and deserializing data.
    Different serialization formats (JSON, Pickle, etc) should use this interface.
    """
    @abstractmethod
    def serialize(self, data: Dict[str, Any]) -> Union[str, bytes]:
        """
        Serializes a dictionary of data to a string or bytes.

        Args:
            data: Dictionary to serialize

        Returns:
            Serialized representation of the data
        """
        pass

    @abstractmethod
    def deserialize(self, data: Union[str, bytes]) -> Dict[str, Any]:
        """
        Deserializes a string or bytes back to a dictionary.

        Args:
            data: Serialized data to deserialize

        Returns:
            Deserialized dictionary
        """
        pass