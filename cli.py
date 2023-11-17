import typer
from typing_extensions import Annotated

from app.cli.handler import PixelArtHandlerApp

app = typer.Typer()
@app.command()
def main(
  image: Annotated[str, typer.Argument()],
  pixelSize:Annotated[int, typer.Option()] = 7,
  save: Annotated[bool, typer.Option()] = False,
  fileName: Annotated[str, typer.Option()] = None):
  handler = PixelArtHandlerApp()
  handler.openImage(image)
  handler.setPixelSize(pixelSize)
  handler.run(save, fileName)

if __name__ == "__main__":
  app()
