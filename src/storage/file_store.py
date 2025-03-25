import os
import threading
import time

from typing import Dict, Any, List, Tuple, Optional

from src.storage.serializer_interface import SerializerInterface
from src.storage.storage_interface import StorageInterface
from src.utils.exceptions import StorageError


class FileStorage(StorageInterface):
    """
    File-based implementation of the storage interface.
    Stores key-value pairs in a file with periodic snapshots.
    """

    def __init__(self,
                 file_path: str,
                 serializer: SerializerInterface,
                 snapshot_interval: int = 60 # Seconds
                 ):
        """
         Initialize the file-based storage.

         Args:
             file_path: Path to the file used for storage
             serializer: Serializer to use for data conversion
             snapshot_interval: How often to save snapshots to disk (in seconds)
         """
        self._file_path = file_path
        self._serializer = serializer
        self._snapshot_interval = snapshot_interval
        self._data: Dict[str, Any] = {}
        self._lock = threading.RLock()
        self._last_snapshot_time = 0

        # Create directory if it does not exist
        os.makedirs(os.path.dirname(self._file_path), exist_ok=True)

        # Load any data already stored, if it exists
        self._load_from_file()

        # Start a background Thread for periodic snapshots
        if self._snapshot_interval > 0:
            self._snapshot_thread = threading.Thread(
                target=self._periodic_snapshot,
                daemon=True,
            )
            self._snapshot_thread.start()

    def _load_from_file(self) -> None:
        """
        Load data from file if it exists.

        Returns:
            None
        """
        with self._lock:
            if os.path.exists(self._file_path) and os.path.getsize(self._file_path) > 0:
                try:
                    with open(self._file_path, 'r') as f:
                        serialized_data = f.read()
                        self._data = self._serializer.deserialize(serialized_data)
                except Exception as e:
                    raise StorageError(f"Failed to load data from file: {str(e)}")

    def _save_to_file(self) -> None:
        """
        Saves data to file

        Returns:
             None
        """
        with self._lock:
            try:
                serialized_data = self._serializer.serialize(self._data)
                with open(self._file_path, 'a') as f:
                    f.write(serialized_data)
                self._last_snapshot_time = time.time()
            except Exception as e:
                raise StorageError(f"Failed to save data to file: {str(e)}")

    def _periodic_snapshot(self):
        """
        Periodically save snapshots to disk

        Returns:
            None
        """
        while True:
            # Check every second
            time.sleep(1)
            current_time = time.time()
            if current_time - self._last_snapshot_time >= self._snapshot_interval:
                try:
                    self._save_to_file()
                except Exception as e:
                    # Log the error but don't crash the thread
                    print(f"Error in periodic snapshot: {str(e)}")

    def get(self, key: str) -> Any:
        pass

    def put(self, key: str, value: Any) -> None:
        pass

    def delete(self, key: str) -> bool:
        pass

    def contains(self, key: str) -> bool:
        pass

    def clear(self) -> None:
        pass

    def keys(self) -> List[str]:
        pass

    def items(self) -> List[Tuple[str, Any]]:
        pass

    def size(self) -> int:
        pass