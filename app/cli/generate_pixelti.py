import os
import uuid
from urllib.request import urlretrieve

import validators
from PIL import Image

from core.display import ShellPixel
from core.pallete import BOF, Pallette
from core.pixelti import Pixelti


def getFromInternet(url:str)->Image.Image:
    urlretrieve(url, 'tmp.jpg')
    img = Image.open('tmp.jpg')
    os.remove('tmp.jpg')
    return img

def getFromLocal(url:str)->Image.Image:
    return Image.open(url)

def openImage(url: str) -> Image.Image:
    if(validators.url(url)):
      return getFromInternet(url)
    return getFromLocal(url)

def handleGeneratePixelti(imageUrl: str, pixelSize: int, save: bool, fileName: str = str(uuid.uuid4())+'.jpg'):
    image = openImage(imageUrl)
    pallette = Pallette(BOF)
    pixelti = Pixelti(pallette)
    pixelti.setPixelSize(pixelSize)
    pixelti.setImage(image)
    pixelArt = pixelti.generate()

    if save:
      name = fileName if fileName else str(uuid.uuid4())+'.jpg'
      pixelArt.save(name)

    # to show to console
    # the image will be compressed to thumbnail size
    pix = ShellPixel()
    pixelArt.thumbnail((60, pixelti.imgH * (60 / pixelti.imgW)), resample=Image.Resampling.HAMMING)
    for i in range(pixelArt.size[1]):
      for j in range(pixelArt.size[0]):
        pix.put(pixelArt.getpixel((j, i)))
      pix.endLine()
