"""
Imperative Paradigm – Traffic Light Simulation
Simulates a traffic light system (Green -> Yellow -> Red).
Outputs the current light every second.
Focus: step-by-step control using variables and loops.
"""

import time

def traffic_light():
    lights = ["Green", "Yellow", "Red"]
    current = 0

    while True:
        print(f"Light: {lights[current]}")
        time.sleep(1)
        current = (current + 1) % len(lights)

if __name__ == "__main__":
    traffic_light()
