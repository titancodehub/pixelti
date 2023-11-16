import typer
from typing_extensions import Annotated
from app.cli.generator import PixelArtGeneratorApp


app = typer.Typer()
@app.command()
def main(
  image: Annotated[str, typer.Argument()],
  pixelSize:Annotated[int, typer.Option()] = 7,
  save: Annotated[bool, typer.Option()] = False,
  fileName: Annotated[str, typer.Option()] = None):
  generator = PixelArtGeneratorApp()
  generator.openImage(image)
  generator.setPixelSize(pixelSize)
  generator.run(save, fileName)

if __name__ == "__main__":
  app()