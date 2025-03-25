# Distributed Key-Value Store

A distributed key-value storage system built in Python. This project implements a simple yet robust key-value store that can be scaled to a distributed environment.

## Project Status

Currently implementing the core foundation and single-node functionality:

- [x] Day 1: Basic key-value store with in-memory storage
- [x] Day 2: Persistence layer with file-based storage
- [ ] Day 3: HTTP API and client interface
- [ ] Day 4-7: Node discovery and cluster formation
- [ ] Day 8-10: Data partitioning and replication
- [ ] Day 11-14: Consistency and fault tolerance
- [ ] Day 15-21: Advanced features and optimizations

## Features Implemented

### Storage Engine
- In-memory storage with thread-safety
- File-based persistence with automatic snapshots
- Serialization framework with JSON support

### Core Operations
- Basic CRUD operations (get, put, delete)
- Additional utility methods (contains, clear, keys, items, size)
- Error handling for common failure scenarios

## Getting Started

### Prerequisites
- Python 3.8+
- pytest for running tests

### Installation
1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv .venv
source .