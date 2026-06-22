# config_files/inputs_list.py

# Define valid discrete actions for the Trackmania agent
# This matches the Linesight specs to prevent the AI from inputting nonsense.
ACTIONS = [
    {"forward": True, "backward": False, "left": False, "right": False},  # Straight
    {"forward": True, "backward": False, "left": True, "right": False},   # Accelerate Left
    {"forward": True, "backward": False, "left": False, "right": True},   # Accelerate Right
    {"forward": False, "backward": True, "left": False, "right": False},  # Brake/Reverse
    {"forward": True, "backward": True, "left": True, "right": False},    # Drift Left (example)
    {"forward": True, "backward": True, "left": False, "right": True},    # Drift Right (example)
]