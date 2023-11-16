import numpy as np
from PIL import Image


class Pixelti:
  img: np.ndarray
  imgW: int
  imgH: int
  # compressed dimention is the dimention of the copressed image
  # after we combained pixelSize x pixelSize of the original image into one pixel in the new image
  compressedW: int
  compressedH: int
  pixelSize: int = 7

  def setImage(self, img: Image.Image):
    self.img = np.array(img)
    (self.imgH, self.imgW, _) = self.img.shape
    self.compressedH = self.imgH // self.pixelSize
    self.compressedW = self.imgW // self.pixelSize

  def setPixelSize(self, pixelSize: int):
    self.pixelSize = pixelSize

  def generate(self) -> Image.Image:
    i = 0
    area = self.pixelSize * self.pixelSize

    newImage  = np.zeros(shape=(self.imgH, self.imgW, 3), dtype=np.uint8)
    thumbnail = np.zeros(shape = (self.imgH * (600//self.imgW), 600), dtype=np.uint8)

    for i in range(self.compressedH):
      for j in range(self.compressedW):
        offset1 = i * self.pixelSize
        sumR = 0
        sumG = 0
        sumB = 0
        # compress pixelSize x pixelSize into one pixel
        for k in range(offset1, offset1 + self.pixelSize):
          offset2 = j * self.pixelSize
          for l in range(offset2, offset2 + self.pixelSize):
            sumR += self.img[k][l][0]
            sumG += self.img[k][l][1]
            sumB += self.img[k][l][2]
        rgbAvg = [round(sumR/area, 0), round(sumG/area, 0), round(sumB/area, 0)]

        # restore compressed image to original size
        # by applying the same rgbAvg to the original image
        for m in range(offset1, offset1 + self.pixelSize):
          offset2 = j * self.pixelSize
          for n in range(offset2, offset2 + self.pixelSize):
            newImage[m][n] = rgbAvg

    res = Image.fromarray(newImage)
    return res