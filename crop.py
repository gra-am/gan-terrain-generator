# Improting Image class from PIL module
import time
import glob
from PIL import Image
import uuid

images = glob.glob(r"C:\Users\Graham\Desktop\python\terrain\gan-terrain-generator\images\pre-crop\*.png")

for image in images:
        img = Image.open(image)

        cropped = img.crop((0,0,512,512))
        cropped1 = img.crop((256,0,768,512))
        cropped2 = img.crop((0,256,512,768))
        cropped3 = img.crop((256,256,768,768))

        for c in [cropped, cropped1, cropped2, cropped3]:
            savedir = "C:/Users/Graham/Desktop/python/terrain/gan-terrain-generator/images/post-crop/"
            unique = str(uuid.uuid4())
            filename = savedir + unique + ".png"
            c.save(filename)
