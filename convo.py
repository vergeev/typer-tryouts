import typer

app = typer.Typer()


@app.command()
def say_hello(name: str = typer.Argument(..., help="The name of the person to greet")) -> None:
    typer.secho(f"Hello {name}", fg=typer.colors.MAGENTA)


@app.command()
def show_status(good: bool = True) -> None:
    message_start = "everything is "
    if good:
        ending = typer.style("good", fg=typer.colors.GREEN, bold=True)
    else:
        ending = typer.style("bad", fg=typer.colors.RED, bg=typer.colors.BLACK)
    message = message_start + ending
    typer.echo(message)


@app.command()
def say_goodbye(name: str, formal: bool = False) -> None:
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


if __name__ == "__main__":
    app()
