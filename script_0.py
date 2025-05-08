import pyautogui
from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        # Get the RGB value at the clicked position
        pixel_color = pyautogui.screenshot().getpixel((x, y))
        print(f"Clicked at ({x}, {y}) - Color: {pixel_color}")


with mouse.Listener(on_click=on_click) as listener:
    listener.join()
