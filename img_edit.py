#!/usr/bin/env python3
import os
from PIL import Image, ImageEnhance, ImageFilter # Pillow

__version__ = "0.1.0" # 2023/02

path = "./imgs"
path_out = "./imgs_edited"


for filename in os.listdir(path):
    print(filename)
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert("L").rotate(-90)
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f"{path_out}/{clean_name}_e.jpg")
