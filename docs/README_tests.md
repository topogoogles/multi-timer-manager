# Testing Documentation for Multi-Timer Manager

This document provides an overview of the testing framework for the **Multi-Timer Manager** application. It explains the purpose of the tests, describes the functionality of the `tests/test_multi_timer_manager.py` file, and provides step-by-step instructions for running the tests.

## **Purpose of the Tests**

The tests are designed to ensure that the core functionality of the **Multi-Timer Manager** application works as expected. They validate key components such as:

- The sound notification system.
- Timer duration conversions.
- Timer completion logic.
- The integrity of history data structures.

By running these tests, developers can confirm that changes to the codebase do not introduce bugs or regressions.

## **Overview of `tests/test_multi_timer_manager.py`**

The test file `tests/test_multi_timer_manager.py` contains unit tests written using the `pytest` framework. These tests cover specific functionalities of the application:

### **Test Cases**

1. **Sound Alert Functionality (`test_play_sound_alert`)**
    - Verifies that the `play_sound_alert()` function executes without errors across different platforms (Windows, macOS, Linux).
    - Ensures cross-platform compatibility for sound notifications.
2. **Timer Duration Conversion (`test_timer_duration_conversion`)**
    - Validates that user-entered durations (in minutes, hours, or days) are correctly converted to seconds.
    - Ensures accurate time calculations for timers.
3. **Timer Completion Logic (`test_timer_completion`)**
    - Simulates a completed timer and verifies that it is marked as "completed" when elapsed time meets or exceeds its duration.
    - Ensures timers transition to a completed state correctly.
4. **History Data Structure Integrity (`test_history_data_structure`)**
    - Checks that completed timers added to history maintain the correct data structure (a list of dictionaries).
    - Ensures required keys like `name`, `tags`, and `end_time` are present in history entries.

## **How to Execute the Tests**

Follow these steps to run the tests:

### **Step 1: Set Up Your Environment**

1. Ensure you have Python installed (version >= 3.11).

2. Install [UV](https://astral.sh/uv/) for managing dependencies:

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

3. Activate your virtual environment:

    ```bash
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

4. Install project dependencies:

    ```bash
    uv sync
    ```

### **Step 2: Run Tests**

1. Navigate to the project root directory:

    ```bash
    cd /path/to/multi-timer-manager
    ```

2. Run all tests using `pytest`:

    ```bash
    pytest tests/
    ```

3. To run a specific test case (e.g., `test_play_sound_alert`), use:

    ```bash
    pytest -k test_play_sound_alert
    ```

4. View detailed output by adding the `-v` flag:

    ```bash
    pytest -v tests/
    ```

## **Test Output**

When you run the tests, you should see output similar to this:

```plaintext
==================== test session starts ====================
platform win32 -- Python 3.11.11, pytest-8.3.4
rootdir: C:\Users\arauj\Projects\multi-timer-manager
collected 4 items

tests/test_multi_timer_manager.py ....                [100%]

==================== 4 passed in 0.42s ======================
```

Each dot (`.`) represents a passing test case.

## **Troubleshooting**

If you encounter issues while running tests:

1. **Ensure Dependencies Are Installed**:
Run `uv sync` to make sure all dependencies are installed.

2. **Verify Import Paths**:
If you see an error like `ModuleNotFoundError: No module named 'src'`, ensure your project structure includes an empty `__init__.py` file in the `src/` directory and that you're running `pytest` from the project root.

3. **Check Python Version**:
Ensure you're using Python >= 3.11 by running:

    ```bash
    python --version
    ```

4. **Recreate Virtual Environment** (if necessary):

    ```bash
    rm -rf venv/
    uv sync
    ```

## **Adding New Tests**

To add new test cases:

1. Create or edit files in the `tests/` directory.

2. Write test functions using Python's built-in `unittest` or `pytest`.

3. Follow naming conventions (`test_<functionality>.py`) for discoverability.

4. Run all tests to ensure they pass before committing changes.

Example of a new test case:

```python
def test_example():
    assert 1 + 1 == 2, "Math is broken!"
```

## **Notes**

- For more information on writing tests with Pytest, visit [Pytest Documentation](https://docs.pytest.org/).
- Always run tests after making changes to ensure no functionality is broken.
- Use version control (e.g., Git) to track changes and collaborate with your team effectively.
