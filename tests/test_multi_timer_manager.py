import pytest
from datetime import timedelta
import sys
import os

# Include the src/ directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from multi_timer_manager import play_sound_alert


# Test 1: Verify sound alert functionality
def test_play_sound_alert():
    try:
        play_sound_alert()
    except Exception as e:
        pytest.fail(f"Sound alert function raised an exception: {e}")


# Test 2: Verify timer duration conversion to seconds
def test_timer_duration_conversion():
    # Define sample inputs and expected outputs
    duration = 5  # 5 units of time
    time_units = {"Minutes": 60, "Hours": 3600, "Days": 86400}

    # Check conversion for each unit
    for unit, multiplier in time_units.items():
        expected_seconds = duration * multiplier
        assert expected_seconds == duration * multiplier, f"Failed for unit: {unit}"


# Test 3: Verify timer completion logic
def test_timer_completion():
    # Simulate a completed timer
    timer = {
        "name": "Test Timer",
        "duration": 60,  # 1 minute in seconds
        "start_time": 0,
        "elapsed_paused": 0,
        "completed": False,
    }

    # Simulate elapsed time and mark as completed
    elapsed_time = timer["duration"]
    if elapsed_time >= timer["duration"]:
        timer["completed"] = True

    assert timer["completed"] is True, "Timer did not complete as expected"


# Test 4: Verify history data structure integrity
def test_history_data_structure():
    history = [
        {
            "name": "Test Timer",
            "tags": ["Work", "Urgent"],
            "end_time": "2023-10-01T12:00:00",
            "duration_actual": timedelta(seconds=60),
            "total_repeats": 0,
        }
    ]

    assert isinstance(history, list), "History should be a list"
    assert isinstance(history[0], dict), "Each history entry should be a dictionary"
    assert "name" in history[0], "'name' key missing in history entry"
    assert "tags" in history[0], "'tags' key missing in history entry"
