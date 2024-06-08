from PIL import Image, ImageEnhance, ImageFilter
import os

# Define the path to the directory containing the images to be processed
path = './image-enhancer/images'

# Define the path to the directory where the edited images will be saved
pathOut = './image-enhancer/edited-images'

# Iterate through each file in the directory
for filename in os.listdir(path):
    # Open an image file
    img = Image.open(f"{path}/{filename}")

    # Apply a sharpen filter to the image
    edit = img.filter(ImageFilter.SHARPEN)

    # Convert the image to 'RGB' mode if it is in 'RGBA' mode
    if edit.mode == 'RGBA':
        edit = edit.convert('RGB')

    # Get the filename without the file extension
    clean_name = os.path.splitext(filename)[0]

    # Save the edited image to the output directory with a new name
    edit.save(f'{pathOut}/{clean_name}_edited.jpg')
