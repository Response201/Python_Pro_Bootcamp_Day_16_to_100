import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

def open_image():
    global file_path
    file_path = filedialog.askopenfilename()
    label.config(text=f"Vald bild: {file_path}")


def add_watermark():
    if not file_path:
        label.config(text="Ingen bild vald!")
        return

    text = entry.get()
    image = Image.open(file_path).convert("RGBA")


    max_size = (800, 800)
    image.thumbnail(max_size)

    txt_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)

    width, height = image.size

    try:
        font = ImageFont.truetype("arial.ttf", 50)
    except:
        font = ImageFont.load_default()


    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = ((width - text_width) // 2, (height - text_height) // 2)

    draw.text(position, text, fill=(255, 255, 255, 180), font=font)

    combined = Image.alpha_composite(image, txt_layer)

    save_path = filedialog.asksaveasfilename(defaultextension=".jpg")

    if save_path:
        combined.convert("RGB").save(save_path)
        label.config(text="Sparad!")




root = tk.Tk()
root.title("Watermark App")

file_path = ""

btn_open = tk.Button(root, text="Välj bild", command=open_image)
btn_open.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)
entry.insert(0, "Watermark")

btn_watermark = tk.Button(root, text="Lägg watermark & spara", command=add_watermark)
btn_watermark.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()