# MULTI-TIMER MANAGER WITH ENHANCED FEATURES
# A Streamlit web application for managing multiple timers with notifications, tags, history tracking, and data visualization.

# Import required libraries
import streamlit as st
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import platform
import simpleaudio as sa
import numpy as np

# Conditional import for sound notifications
if platform.system() == "Windows":
    import winsound

from streamlit_tags import st_tags

# Initialize session state
if "timers" not in st.session_state:
    st.session_state.timers = []
if "history" not in st.session_state:
    st.session_state.history = []


# Sound notification function with cross-platform support
def play_sound_alert():
    """Play system default alert sound when timer completes"""
    if platform.system() == "Windows":
        try:
            winsound.PlaySound(
                "SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC
            )
        except Exception as e:
            st.error(f"Sound error: {str(e)}")
    elif platform.system() == "Darwin":  # macOS
        import os

        os.system("afplay /System/Library/Sounds/Ping.aiff")
    elif platform.system() == "Linux":
        import os

        os.system("aplay /usr/share/sounds/sound-icons/trumpet-12.wav")
    else:
        # Fallback using simpleaudio
        frequency = 440  # Hz, waves per second
        length = 1  # second
        sample_rate = 44100
        t = np.linspace(0, length, int(sample_rate * length), False)
        note = np.sin(frequency * t * 2 * np.pi)
        audio = note * (32767 / np.max(np.abs(note)))
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
        play_obj.wait_done()


# =====================
# USER INTERFACE SETUP
# =====================

# Main header
st.title("Multi-Timer Manager")

# ---------------------
# TIMER CREATION SIDEBAR
# ---------------------
with st.sidebar:
    st.header("Create New Timer")

    # Timer configuration inputs
    timer_name = st.text_input(
        "Timer Name", help="Enter a descriptive name for your timer"
    )
    duration = st.number_input("Duration", min_value=1, value=30, help="Duration value")
    time_unit = st.selectbox(
        "Time Unit", ["Minutes", "Hours", "Days"], help="Select time measurement unit"
    )
    timer_color = st.color_picker(
        "Select Timer Color", "#4B9CD3", help="Choose a color for visual identification"
    )

    # Tag management with suggested categories
    tags = st_tags(
        label="Add Tags:",
        text="Press enter to add",
        value=[],
        suggestions=["Work", "Personal", "Urgent"],
    )

    # Repeat functionality
    repeats = st.number_input(
        "Repeat Count",
        min_value=0,
        value=0,
        help="Number of automatic repetitions (0 = single use)",
    )

    # Timer creation logic
    if st.button("Add Timer"):
        # Convert duration to seconds based on selected unit
        multiplier = {"Minutes": 60, "Hours": 3600, "Days": 86400}[time_unit]

        # Timer data structure
        timer_data = {
            "name": timer_name,  # Timer display name
            "duration": duration * multiplier,  # Total duration in seconds
            "color": timer_color,  # UI color
            "tags": tags,  # Categorization tags
            "start_time": time.time(),  # Unix timestamp of creation
            "paused": False,  # Pause state
            "elapsed_paused": 0,  # Accumulated paused time
            "completed": False,  # Completion status
            "repeats_left": repeats,  # Remaining repetitions
            "total_repeats": repeats,  # Original repeat count
        }
        st.session_state.timers.append(timer_data)

# --------------------
# ACTIVE TIMERS DISPLAY
# --------------------
st.header("Active Timers")
for idx, timer in enumerate(
    st.session_state.timers[:]
):  # Iterate over copy for safe modification
    if not timer["completed"]:
        with st.container(border=True):  # Visual container for each timer
            cols = st.columns([3, 1, 1, 1])  # Create layout columns

            # Timer info column
            with cols[0]:
                st.subheader(timer["name"])
                st.caption(
                    f"Tags: {', '.join(timer['tags'])}" if timer["tags"] else "No tags"
                )
                st.color_picker("", timer["color"], disabled=True, key=f"color_{idx}")

                # Time calculation logic
                if not timer["paused"]:
                    elapsed = (
                        time.time() - timer["start_time"] - timer["elapsed_paused"]
                    )
                else:
                    elapsed = timer["elapsed_paused"]

                remaining = max(timer["duration"] - elapsed, 0)
                progress = min(elapsed / timer["duration"], 1.0)

                # Progress bar with time formatting
                st.progress(
                    progress,
                    f"Time remaining: {datetime.timedelta(seconds=int(remaining))} | "
                    + f"Repeats left: {timer['repeats_left']}",
                )

            # Control buttons column
            with cols[1]:  # Pause/Resume toggle
                if st.button(
                    "â¸ï¸" if not timer["paused"] else "â–¶ï¸", key=f"pause_{idx}"
                ):
                    timer["paused"] = not timer["paused"]
                    if timer["paused"]:
                        # Store elapsed time when pausing
                        timer["elapsed_paused"] = time.time() - timer["start_time"]
                    else:
                        # Reset start time when resuming
                        timer["start_time"] = time.time()

            with cols[2]:  # Reset button
                if st.button("ðŸ”„", key=f"reset_{idx}"):
                    # Reset timer to initial state
                    timer["start_time"] = time.time()
                    timer["elapsed_paused"] = 0
                    timer["paused"] = False

            with cols[3]:  # Complete button
                if st.button("âœ“", key=f"complete_{idx}"):
                    timer["completed"] = True
                    play_sound_alert()  # Audible notification

                    # Add to history with completion details
                    st.session_state.history.append(
                        {
                            **timer,
                            "end_time": datetime.datetime.now().isoformat(),
                            "duration_actual": elapsed,
                        }
                    )

                    # Handle timer repetitions
                    if timer["repeats_left"] > 0:
                        new_timer = {
                            **timer,
                            "start_time": time.time(),
                            "paused": False,
                            "elapsed_paused": 0,
                            "completed": False,
                            "repeats_left": timer["repeats_left"] - 1,
                        }
                        st.session_state.timers.append(new_timer)

# ----------------------
# HISTORY & DATA EXPORT
# ----------------------
st.header("History & Export")
if st.session_state.history:
    # Create DataFrame from history data
    history_df = pd.DataFrame(st.session_state.history)[
        ["name", "tags", "end_time", "duration_actual", "total_repeats"]
    ]

    # Display formatted history with color coding
    st.dataframe(
        history_df.style.apply(
            lambda x: [f"background-color: {row['color']}" for row in x], axis=1
        ),
        use_container_width=True,
    )

    # CSV export functionality
    if st.button("Export History to CSV"):
        csv = history_df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="timer_history.csv",
            mime="text/csv",
        )
else:
    st.info("No completed timers yet")

# --------------------
# ADVANCED STATISTICS
# --------------------
st.header("Advanced Statistics")
if st.session_state.timers or st.session_state.history:
    # Prepare data for visualizations
    df = pd.DataFrame(
        [
            {
                "Task": t["name"],
                "Duration": t["duration"],
                "Tags": ", ".join(t["tags"]),
                "Color": t["color"],
                "Repeats": t["total_repeats"] + 1,  # Include initial run + repeats
            }
            for t in st.session_state.timers + st.session_state.history
        ]
    )

    # Create tabbed visualization interface
    tab1, tab2 = st.tabs(["Time Distribution", "Tag Analysis"])

    with tab1:  # Pie chart of time allocation
        fig, ax = plt.subplots()
        df.groupby("Task")["Duration"].sum().plot(
            kind="pie", colors=df["Color"].unique(), autopct="%1.1f%%", ax=ax
        )
        st.pyplot(fig)

    with tab2:  # Bar chart of tag frequency
        tag_counts = df["Tags"].str.split(", ").explode().value_counts()
        st.bar_chart(tag_counts)
else:
    st.info("No timers yet - create your first timer using the sidebar!")
