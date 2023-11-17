import math


def createChunks(iterable, n=3):
  chunkSize = math.ceil(len(iterable) / n)
  return [iterable[i:i+chunkSize] for i in range(0, len(iterable), chunkSize)]

def hexToRGB(hex: str) -> tuple:
  if len(hex) != 6:
    raise Exception('Hex must have 6 characters')
  return (int(hex[0:2], 16), int(hex[2:4], 16), int(hex[4:6], 16))