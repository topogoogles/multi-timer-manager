# Multi-Timer Manager

A Streamlit web application designed to manage multiple timers with features like notifications, tags, history tracking, and data visualization.

## Overview

This project provides a user-friendly interface for creating and managing multiple timers. It supports customizable timer names, durations, colors, and tags. The application also includes features for pausing, resetting, and completing timers, with sound notifications upon completion. Additionally, it tracks timer history and offers data visualization to analyze time usage.

## Features

- **Timer Creation**: Easily create new timers with customizable names, durations, colors, and tags.
- **Real-time Updates**: View active timers with real-time progress bars and remaining time displays.
- **Control Options**: Pause, reset, or complete timers as needed.
- **Sound Notifications**: Receive audible alerts when timers complete.
- **History Tracking**: Store and display completed timer records.
- **Data Visualization**: Analyze time allocation and tag usage through interactive charts.
- **Testing**: Includes a comprehensive suite of tests to ensure functionality.

## Requirements

- **Python 3.11+**: Required for running the application.
- **UV**: A fast and modern Python package manager.
- Dependencies listed in `pyproject.toml`.

## Setup

### Step 1: Clone the Repository

```bash

git clone https://github.com/topogoogles/multi-timer-manager.git
cd multi-timer-manager

```

### Step 2: Install UV (if not already installed)

```bash

curl -LsSf https://astral.sh/uv/install.sh | sh

```

Make sure `uv` is in your PATH.

### Step 3: Create and Activate Virtual Environment

```bash

uv venv venv

```

- Activate virtual environment
  - Windows:
    .\venv\Scripts\activate
  - macOS/Linux:
    source venv/bin/activate

### Step 4: Install Dependencies using UV

Initialize UV and sync dependencies based on `pyproject.toml`:

```bash

uv sync

```

This command will read the dependencies listed in `pyproject.toml` and install them into the virtual environment.

### Step 5: Run the Application

```bash

uv run streamlit run src/multi_timer_manager.py

```

## Testing

The project includes a suite of tests to ensure functionality.
See `docs/README_tests.md` for details on how to run the tests.

## Project Structure

```text

multi-timer-manager/
├── src/
│   └── multi_timer_manager.py  \# Main application code
├── tests/
│   └── test_multi_timer_manager.py  \# Test file
├── docs/
│   └── README_tests.md  \# Testing documentation
├── pyproject.toml  \# Project metadata and dependencies
├── pytest.ini    \# Pytest configuration
├── README.md     \# This file
├── uv.lock       \# Dependency lock file
└── LICENSE       \# License file

```

## Contributing

Contributions are welcome! Please submit pull requests with detailed descriptions of changes. Be sure to run the tests before submitting.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgments

- Special thanks to the Streamlit and Streamlit-Tags communities for their support and documentation.
