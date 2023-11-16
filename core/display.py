from colr import Colr as C

class ShellPixel:
  pixel = u"\u2588\u2588"

  def put(self, color=(255,255,255)):
    print(C().rgb(color[0],color[1],color[2], self.pixel), end="")

  def endLine(self):
    print()

class Pallette:
  pallete = None

  def __init__(self, pallete = None):
    self.pallete = pallete

  def convert(self, color=(0,0,0)) -> tuple:
    if self.pallete == None:
      return color

    minDistance = 10000000000000000000 # a very large number
    selectedColor = color
    for colorItem in self.pallete:
      distance = self.__calculateEuclidean(color, colorItem)
      if minDistance > distance:
        minDistance = distance
        selectedColor = colorItem

    return selectedColor

  def __calculateEuclidean(self, vector1: tuple, vector2: tuple):
    if len(vector1) != len(vector2):
      raise Exception('Vectors must have the same length')

    sum = 0
    for i in range(len(vector1)):
      sum += (vector1[i] - vector2[i])**2
    return sum**(1/2)