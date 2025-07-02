# LoggerModule

A Python logging utility with file and stream handlers and automatic fallback options.

## Installation

```bash
pip install LoggerModule
```

## Usage

```python
from LoggerModule import LoggerClass

# Basic usage
logger = LoggerClass("MyApp").get_logger()
logger.info("This is an info message")

# Custom log folder
logger = LoggerClass("MyApp", PathLogFolder="/var/logs/myapp").get_logger()

# Custom format
custom_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logger = LoggerClass("MyApp", FormatLog=custom_format).get_logger()
```

## Features

- Automatic file handler creation
- Fallback to current directory if specified path is not writable
- Customizable log format
- Thread-safe logging
