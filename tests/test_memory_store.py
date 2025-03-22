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

def test_put_twice_same_key_diff_values(memory_store):
    memory_store.put("key", "value1")
    memory_store.put("key", "value2")
    assert memory_store.get("key") == "value2"

def test_contains(memory_store):
    memory_store.put("key3", "value3")
    assert memory_store.contains("key3")

def test_contains_no_element_present(memory_store):
    assert memory_store.contains("key1") == False

def test_clear(memory_store):
    memory_store.put("key", "value")
    memory_store.clear()
    assert memory_store.size() == 0

def test_size(memory_store):
    memory_store.put("key1", "value1")
    memory_store.put("key2", "value2")
    assert memory_store.size() == 2

def test_keys(memory_store):
    memory_store.put("key1", "value1")
    memory_store.put("key2", "value2")
    assert memory_store.keys() == ["key1", "key2"]

def test_items(memory_store):
    memory_store.put("key1", "value1")
    memory_store.put("key2", "value2")
    assert memory_store.items() == [("key1", "value1"), ("key2", "value2")]

def test_concurrent_access(memory_store):
    """Tests concurrent access to the memory store"""
    def writer():
        for i in range(100):
            memory_store.put(f"key{i}", f"value{i}")
            # Small fraction of time to increase chance of race conditions
            time.sleep(0.001)

    def reader():
        for i in range(100):
            memory_store.get(f"key{i}")
            time.sleep(0.001)

    # Create and start threads
    writer_thread = threading.Thread(target=writer)
    reader_thread = threading.Thread(target=reader)

    writer_thread.start()
    reader_thread.start()

    # Wait for threads to complete
    writer_thread.join()
    reader_thread.join()

    # Verify results
    assert memory_store.size() == 100
    for i in range(100):
        assert memory_store.get(f"key{i}") == f"value{i}"