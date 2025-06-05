import pyautogui
import time
import os

def sleep_computer():
    # This command puts Windows to sleep
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

print("Starting prevent sleep...")

try:
    duration_hours = float(input("Enter duration in hours: "))
    duration_seconds = duration_hours * 3600
    duration_seconds = 10  # For testing
    print(f"Preventing sleep for {duration_hours} hours...")
    start_time = time.time()

    while time.time() - start_time < duration_seconds:
        x, y = pyautogui.position()  # Get the current mouse position
        pyautogui.moveTo(x + 5, y + 5, duration=0.1)  # Move the mouse slightly
        pyautogui.moveTo(x - 5, y - 5, duration=0.1)
        # time.sleep(10)
except KeyboardInterrupt:
    print("Stopping prevent sleep...")
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Exiting program.")
    pyautogui.moveTo(0, 0)
    time.sleep(1)  # Wait a moment before exiting
    sleep_computer()  # Put the computer to sleep after duration
    exit(0)
