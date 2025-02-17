
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

## Requirements

- **Python 3.8+**: Required for running the application.
- **Streamlit**: Main framework for the web application.
- **Pandas**: Used for data handling and analysis.
- **Matplotlib**: Provides visualization capabilities.
- **Streamlit-Tags**: Component for tag management.
- **Winsound** (Windows): For sound notifications.

## Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/topogoogles/multi-timer-manager.git
```

### Step 2: Install Dependencies

Use UV for dependency management (install UV if not already installed):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
cd multi-timer-manager
uv init
uv add streamlit pandas matplotlib streamlit-tags pytest
uv add winsound  # For Windows sound support
```

### Step 3: Run the Application

```bash
uv run streamlit run src/multi-timer-manager.py
```

## Contributing

Contributions are welcome! Please submit pull requests with detailed descriptions of changes.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgments

- Special thanks to the Streamlit and Streamlit-Tags communities for their support and documentation.

