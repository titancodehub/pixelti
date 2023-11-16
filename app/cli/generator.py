import os
import uuid
from urllib.request import urlretrieve

from PIL import Image

from core.display import ShellPixel
from core.pixelti import Pixelti


class PixelArtGeneratorApp:
  image: Image.Image
  def openImage(self, url: str):
    if(self.__isHttpUrl(url)):
      self.image = self.__getFromInternet(url)
      return
    self.image = self.__getFromLocal(url)
    return

  def setPixelSize(self, pixelSize: int):
    self.pixelSize = pixelSize

  def run(self, shouldSave = False, fileName: str = None):
    pixelti = Pixelti()
    pixelti.setPixelSize(self.pixelSize)
    pixelti.setImage(self.image)
    pixelArt = pixelti.generate()

    if shouldSave:
      name = fileName if fileName else str(uuid.uuid4())+'.jpg'
      pixelArt.save(name)

    pix = ShellPixel()
    pixelArt.thumbnail((60, pixelti.imgH * (60 / pixelti.imgW)), resample=Image.Resampling.HAMMING)
    for i in range(pixelArt.size[1]):
      for j in range(pixelArt.size[0]):
        pix.put(pixelArt.getpixel((j, i)))
      pix.endLine()

  def __getFromInternet(self, url:str)->Image.Image:
    urlretrieve(url, 'tmp.jpg')
    img = Image.open('tmp.jpg')
    os.remove('tmp.jpg')
    return img

  def __getFromLocal(self, url:str)->Image.Image:
    return Image.open(url)

  def __isHttpUrl(self, url: str):
    method = url.split(':')[0]
    if method in set('http', 'https'):
      return True
    return False