import time
import glob
from PIL import Image
import uuid

## Opens the downloaded image folder and collects the images into a glob.
## I honestly am not sure what a glob actually is.
images = glob.glob(r"C:\Users\Graham\Desktop\python\terrain\gan-terrain-generator\images\pre-crop\*.png")

for image in images:
        img = Image.open(image)

        ## Crops the image into 4 predetermined 512x512 png files.
        ## TODO: make this automatically scale based on input image size.
        cropped = img.crop((0,0,512,512))
        cropped1 = img.crop((256,0,768,512))
        cropped2 = img.crop((0,256,512,768))
        cropped3 = img.crop((256,256,768,768))

        for c in [cropped, cropped1, cropped2, cropped3]:
            savedir = "C:/Users/Graham/Desktop/python/terrain/gan-terrain-generator/images/post-crop/"

            ## This is really cool, it creates a unique string similar to a GUID.
            unique = str(uuid.uuid4())
            filename = savedir + unique + ".png"
            c.save(filename)
