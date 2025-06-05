import pyautogui
import time

print("Starting prevent sleep...")

try:
    while True:

        x,y = pyautogui.position()  # Get the current mouse position
        pyautogui.moveTo(x + 5, y + 5, duration=0.1)  # Move the mouse slightly
        pyautogui.moveTo(x - 5, y - 5, duration=0.1)
        time.sleep(30)
except KeyboardInterrupt:
    print("Stopping prevent sleep...")
    pass
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Exiting program.")
    pyautogui.moveTo(0, 0)
    # Move the mouse to the top-left corner on exit

    time.sleep(1)  # Wait a moment before exiting
    exit(0)
