import pytest
import threading
import time
from src.storage.memory_store import MemoryStore
from src.utils.exceptions import KeyNotFoundError

@pytest.fixture
def memory_store():
    return MemoryStore()

def test_put_and_get(memory_store):
    memory_store.put("key", "value")
    assert memory_store.get("key") == "value"

    """Test overwritting an existing key"""
    memory_store.put("key", "value2")
    assert memory_store.get("key") == "value2"

def test_delete(memory_store):
    memory_store.put("key", "value")
    assert memory_store.get("key") == "value"

    # Delete and assert
    assert memory_store.delete("key") == True
    with pytest.raises(KeyNotFoundError):
        memory_store.get("key")