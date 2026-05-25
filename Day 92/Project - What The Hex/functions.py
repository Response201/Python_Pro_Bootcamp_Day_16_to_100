import os
from PIL import Image

def simplify(color):
    r, g, b = color
    return (r // 30 * 30, g // 30 * 30, b // 30 * 30)



def get_color_palette(image):

    img = Image.open(image).convert("RGB").resize((100, 100))
    pixels = list(img.getdata())

    freq = {}

    for color in pixels:
        color = simplify(color)
        if color in freq:
            freq[color] += 1
        else:
            freq[color] = 1

    palette  = sorted(freq.items(), key=lambda item: item[1], reverse=True)[:10]
    return palette



def save_image(image):

    path = os.path.join("static", "image", "image.jpg")
    image.save(path)

    return "/static/image/" + "image.jpg"


def delete_image():

    path = os.path.join("static", "image", "image.jpg")
    if os.path.exists(path):
        os.remove(path)