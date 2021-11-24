import typer


def callback(ctx: typer.Context):
    ctx.obj = 123
    typer.echo("Running a command")


def result_callback(*args, **kwargs):
    typer.echo("Finishing the command")


app = typer.Typer(callback=callback, result_callback=result_callback)


@app.command()
def create(ctx: typer.Context, name: str):
    typer.echo(f"Creating user: {name}")
    typer.echo(f"ctx.obj: {ctx.obj}")


if __name__ == "__main__":
    app()
