import random

import typer


def generate_random_name() -> str:
    return random.choice(["World", "Cruel World", "Mate", "Ma Man"])


def main(name: str = typer.Argument(generate_random_name)) -> None:
    typer.echo(f"Hello {name}!")


if __name__ == "__main__":
    typer.run(main)
