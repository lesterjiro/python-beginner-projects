from PIL import Image, ImageEnhance, ImageFilter
import os

path = './image-enhancer/images'
pathOut = './image-enhancer/edited-images'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN)

    if edit.mode == 'RGBA':
        edit = edit.convert('RGB')

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{clean_name}_edited.jpg')

