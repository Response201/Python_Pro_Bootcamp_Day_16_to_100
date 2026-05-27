from PIL import ImageGrab
import time
from pynput import keyboard

space_pressed = False

def obstacle_detected():
    pixel = 120
    image = ImageGrab.grab(bbox=(450, 420, 650, 460)).convert("L")
    pixels = image.getdata()

    dark_pixels = 0
    for p in pixels:
        if p < pixel:
            dark_pixels += 1

    return dark_pixels >= 20

def on_press(key):
    global space_pressed
    if key == keyboard.Key.space:
        space_pressed = True

def on_release(key):
    global space_pressed
    if key == keyboard.Key.space:
        space_pressed = False


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

print("Öppna: chrome://dino i din webbläsare")

while True:

    obstacle_detected()
    time.sleep(0.05)