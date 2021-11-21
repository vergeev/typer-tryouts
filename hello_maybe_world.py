import typer


def main(name: str = typer.Argument(None)) -> None:
    if name:
        typer.echo(f"Hello {name}!")
    else:
        typer.echo("Hello World!")


if __name__ == "__main__":
    typer.run(main)
