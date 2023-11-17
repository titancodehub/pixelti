import math


def createChunks(iterable, n=3):
  chunkSize = math.ceil(len(iterable) / n)
  return [iterable[i:i+chunkSize] for i in range(0, len(iterable), chunkSize)]
