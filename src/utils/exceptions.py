class KeyValueStoreError(Exception):
    """Base exception for all key-value store errors."""
    pass

class KeyNotFoundError(KeyValueStoreError):
    """Exception raised when a key is not found in the store."""
    pass

class StorageError(KeyValueStoreError):
    """Exception raised when a storage operation fails."""
    pass

class ConcurrencyError(KeyValueStoreError):
    """Exception raised for concurrency-related errors."""
    pass

class TransactionError(KeyValueStoreError):
    """Exception raised when a transaction operation fails."""
    pass