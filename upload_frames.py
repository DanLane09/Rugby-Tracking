import pyautogui
import time


BUTTON_X = 2500
BUTTON_Y = 275
DELAY_AFTER_CLICK = 1
DELAY_AFTER_TYPE = 0.1
TOTAL_IMAGES_TO_GENERATE = 4000
BATCH_SIZE = 10

print(f"Starting automation. Will generate up to {TOTAL_IMAGES_TO_GENERATE} images.")
print(f"Clicking button at coordinates: ({BUTTON_X}, {BUTTON_Y})")
print("Press Ctrl+C or move mouse to a corner to stop.")

saved_count = 0

try:
    time.sleep(5)
    while saved_count < TOTAL_IMAGES_TO_GENERATE:
        # Click the button
        pyautogui.click(BUTTON_X, BUTTON_Y)
        time.sleep(DELAY_AFTER_CLICK)

        start_range = saved_count
        end_range = min(saved_count + BATCH_SIZE, TOTAL_IMAGES_TO_GENERATE)

        for i in range(start_range, end_range):
            filename = f"\"frame_{i:05d}.jpg\" "
            print(f"Typing: {filename}")
            pyautogui.write(filename)
            # time.sleep(DELAY_AFTER_TYPE)

            saved_count += 1
            if saved_count >= TOTAL_IMAGES_TO_GENERATE:
                break

        pyautogui.press('enter')
        time.sleep(DELAY_AFTER_CLICK)

        print(f"Completed batch. Current total images generated: {saved_count}")

except pyautogui.FailSafeException:
    print("\nPyAutoGUI Fail-Safe triggered. Automation stopped.")
except Exception as e:
    print(f"\nAn error occurred: {e}")
finally:
    print("Script finished.")
