import time
import pyautogui
import tkinter as tk


def screenshot():
    # Create a random name string with digits
    name = int(round(time.time() * 1000))  # generate number
    name = 'screenshots/{}.png'.format(name)
    time.sleep(5)
    # img = pyautogui.screenshot('test.png')
    img = pyautogui.screenshot(name)
    img.show()


# screenshot()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()