from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List, Tuple

class StorageInterface(ABC):
    """
    Abstract base class defining the interface for key-value storage implementations.
    All storage backends (memory, file, etc.) should implement this interface.
    """

    @abstractmethod
    def get(self, key: str) -> Any:
        """
        Retrieves a value by its key.

        Args:
            key: The key to look up

        Returns:
            The value associated with the key

        Raises:
            KeyNotFoundError: If the key doesn't exist in the storage
        """
        pass

    @abstractmethod
    def put(self, key: str, value: Any) -> None:
        """
          Stores a value with the given key.

          Args:
              key: The key to store the value under
              value: The value to store

          Returns:
              None
          """
        pass

    @abstractmethod
    def delete(self, key: str) -> bool:
        """
        Deletes a key-value pair from the storage.

        Args:
            key: The key to delete

        Returns:
            True if the key existed and was deleted, False otherwise
        """
        pass


    @abstractmethod
    def contains(self, key: str) -> bool:
        """
        Checks if a key exists in the storage.

        Args:
            key: The key to check for

        Returns:
            True if the key exists, False otherwise
        """
        pass


    @abstractmethod
    def clear(self) -> None:
        """
        Removes all key-value pairs from the storage.

        Returns:
            None
        """
        pass


    @abstractmethod
    def keys(self) -> List[str]:
        """
        Returns all keys in the storage.

        Returns:
            A list of all keys
        """
        pass


    @abstractmethod
    def items(self) -> List[Tuple[str, Any]]:
        """
        Returns all key-value pairs in the storage.

        Returns:
            A list of (key, value) tuples
        """
        pass


    @abstractmethod
    def size(self) -> int:
        """
        Returns the number of key-value pairs in the storage.

        Returns:
            The number of items stored
        """
        pass
