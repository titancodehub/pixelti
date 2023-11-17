import asyncio

import numpy as np
from PIL import Image

from core.pallete import Pallette
from lib.utils import createChunks


class Pixelti:
  colorPallette: Pallette = None
  img: np.ndarray
  imgW: int
  imgH: int
  # compressed dimention is the dimention of the copressed image
  # after we combained pixelSize x pixelSize of the original image into one pixel in the new image
  compressedW: int
  compressedH: int
  pixelSize: int = 7

  __outputArray: any

  def __init__(self, colorPallette: Pallette = None):
    self.colorPallette = colorPallette

  def setImage(self, img: Image.Image):
    self.img = np.array(img)
    (self.imgH, self.imgW, _) = self.img.shape
    self.compressedH = self.imgH // self.pixelSize
    self.compressedW = self.imgW // self.pixelSize

  def setPixelSize(self, pixelSize: int):
    self.pixelSize = pixelSize

  def setColorPallette(self, colorPallette: Pallette):
    self.colorPallette = colorPallette

  def generate(self) -> Image.Image:
    i = 0
    newImage  = np.zeros(shape=(self.imgH, self.imgW, 3), dtype=np.uint8)
    for i in range(self.compressedH):
      for j in range(self.compressedW):
        offset1 = i * self.pixelSize
        offset2 = j * self.pixelSize
        r = self.img[offset1: offset1+self.pixelSize,offset2: offset2+self.pixelSize,0]
        g = self.img[offset1: offset1+self.pixelSize,offset2: offset2+self.pixelSize,1]
        b = self.img[offset1: offset1+self.pixelSize,offset2: offset2+self.pixelSize,2]

        newColor = [r.mean(), g.mean(), b.mean()]
        if self.colorPallette is not None:
          newColor = self.colorPallette.translateColor(newColor)

        # restore compressed image to original size
        # by applying the same rgbAvg to the original image
        for m in range(offset1, offset1 + self.pixelSize):
          offset2 = j * self.pixelSize
          for n in range(offset2, offset2 + self.pixelSize):
            newImage[m][n] = newColor

    return Image.fromarray(newImage)

  async def _processPixelInParalel(self, index:list):
    for i in index:
      for j in range(self.compressedW):
        offset1 = i * self.pixelSize
        offset2 = j * self.pixelSize
        r = self.img[offset1: offset1+self.pixelSize,offset2: offset2+self.pixelSize,0]
        g = self.img[offset1: offset1+self.pixelSize,offset2: offset2+self.pixelSize,1]
        b = self.img[offset1: offset1+self.pixelSize,offset2: offset2+self.pixelSize,2]
        newColor = [r.mean(), g.mean(), b.mean()]
        if self.colorPallette is not None:
          newColor = self.colorPallette.translateColor(newColor)
        # restore compressed image to original size
        # by applying the same rgbAvg to the original image
        for m in range(offset1, offset1 + self.pixelSize):
          offset2 = j * self.pixelSize
          for n in range(offset2, offset2 + self.pixelSize):
            self.__outputArray[m][n] = newColor

  async def __asyncTask(self) -> None:
    chunk = createChunks([x for x in range(self.compressedH)], 50)
    self.__outputArray = np.zeros(shape=(self.imgH, self.imgW, 3), dtype=np.uint8)
    asyncio.gather(*[self._processPixelInParalel(task) for task in chunk])

  def generateInParalel(self) -> Image.Image:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(self.__asyncTask())
    loop.close()
    return Image.fromarray(self.__outputArray)

