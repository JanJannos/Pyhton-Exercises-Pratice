import time
import pyautogui
import tkinter as tk


def screenshot():
    # Create a random name string with digits
    name = int(round(time.time() * 1000))  # generate number
    name = 'screenshots/{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot('test.png')
    img = pyautogui.screenshot(name)
    img.show()


# screenshot()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# create 2 buttons

button = tk.Button(frame, text="Take ScreenShot", command=screenshot)
button.pack(side=tk.LEFT)
close = tk.Button(frame, text="QUIT", command=quit)
close.pack(side=tk.LEFT)

# Run the UI
root.mainloop()
