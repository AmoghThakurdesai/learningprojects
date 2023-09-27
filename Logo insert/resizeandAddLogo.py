# python3
# resizeandAddLogo.py - Resize all images in the cwd to fit
# to fit in a 300x300 square and adds catlogo.png to a lower right corner
from PIL import Image

import os

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm=Image.open(LOGO_FILENAME)
logoIm=logoIm.resize((int(SQUARE_FIT_SIZE/5),int(SQUARE_FIT_SIZE/5)))
logoWidth,logoHeight=logoIm.size

os.makedirs('withlogo',exist_ok=True)
# TODO: Loop over all files in the working directory
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
        or filename == LOGO_FILENAME:
        continue  # skip non image files and logo file itself

    im = Image.open(filename)
    width,height = im.size
# TODO: Check if images needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # TODO: Calculate te new widht and height to resize to
        if width > height:
            height = int((SQUARE_FIT_SIZE / width)* height)
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
# TODO: Resize the image
    print(f'Resizing {filename}....')
    im.resize((width,height))
# TODO: Add the logo
    print(f'Adding logo to {filename}....')
    im.paste(logoIm,(width - logoWidth,height - logoHeight),logoIm)
# TODO: Save changes
    im.save(os.path.join('withlogo',filename))
