import numpy as np
import os
import skimage
from PIL import Image

## Simple implementation of the mean squared error between two images.
def mse(imgA, imgB):
    return np.sqrt(((skimage.img_as_float(imgA) - skimage.img_as_float(imgB)) ** 2).mean())

## TODO: Implement better testing of "validity" and collect more data to test against.

## Opening a sample of a real world heightmap.
realImg = Image.open(r"C:\Users\Graham\Desktop\python\terrain\gan-terrain-generator\images\scoring\real.png")

## Opening a sample of a generated heightmap.
ganImg = Image.open(r"C:\Users\Graham\Desktop\python\terrain\gan-terrain-generator\images\scoring\gan.png")

## Opening a sample of a heightmap made from random noise.
noiseImg = Image.open(r"C:\Users\Graham\Desktop\python\terrain\gan-terrain-generator\images\scoring\noise.png")

print("Mse accuracy for generated image comparison:" + str(np.round((1.0 - mse(realImg, ganImg)), 4)))
print("Mse accuracy for noise image comparison:" + str(np.round((1.0 - mse(realImg, noiseImg)), 4)))
