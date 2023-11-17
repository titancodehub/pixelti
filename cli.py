import time

import typer
from typing_extensions import Annotated

from app.cli.generate_pixelti import handleGeneratePixelti

app = typer.Typer()
@app.command()
def main(
  image: Annotated[str, typer.Argument()],
  pixelSize:Annotated[int, typer.Option()] = 7,
  save: Annotated[bool, typer.Option()] = False,
  fileName: Annotated[str, typer.Option()] = None):
  startTime = time.time()
  handleGeneratePixelti(image, pixelSize, save, fileName)
  print("\n")
  print("Execution Time: %0.3f seconds"%(time.time() - startTime))

if __name__ == "__main__":
  app()
