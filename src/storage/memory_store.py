import threading
from typing import Dict, Any, Optional, List, Tuple
from src.utils.exceptions import KeyNotFoundError

class MemoryStore:
    """
    Simple in-memory key-value store
    This is the foundation for a distributed key-value database
    """
    def __init__(self):
        """
        Initialise an empty key-value store with a thread for locking transactions
        """
        self._data: Dict[str, Any] = {}
        self._lock = threading.RLock() #Re-entrant lock for thread safety

    def get(self, key: str) -> Any:
        """
        Returns a stored entity based on a key, if it exists.
        :param key: Key for the stored entity
        :return: The entity associated with the key
        """
        with self._lock:
            if key not in self._data:
                raise KeyNotFoundError
            return self._data[key]

    def put(self, key: str, value: Any) -> None:
        """
        Stores a value based on a key
        :param key: Key of value to be stored
        :param value: Value to be stored
        :return: None
        """
        with self._lock:
            self._data[key] = value

    def delete(self, key: str) -> bool:
        """
        Deletes a value from the storage
        :param key: Key of value to be deleted
        :return: Result of the operation
        """
        with self._lock:
            if key in self._data:
                del self._data[key]
                return True
            return False

    def contains(self, key) -> bool:
        """
        Checks whether value exists for the given key
        :param key: Key of the value to check for
        :return: Result of the operation
        """
        with self._lock:
            return key in self._data

    def clear(self) -> None:
        """
        Clears the storage of all values.
        :return: None
        """
        with self._lock:
            self._data.clear()

    def keys(self) -> List[str]:
        """
        Returns all the keys in the storage.
        :return: List of storage keys
        """
        with self._lock:
            return list(self._data.keys())

    def items(self) -> List[Tuple[str, Any]]:
        """
        Returns all the items in the storage
        :return: List of tuples corresponding to the key-value items
        """
        with self._lock:
            return list(self._data.items())

    def size(self) -> int:
        """
        Returns the size of items in the storage
        :return: Number of items in the storage
        """
        with self._lock:
            return len(self._data)

