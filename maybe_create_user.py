import typer


existing_usernames = ["john doe", "jane doe"]


def maybe_create_user(username: str) -> None:
    if username in existing_usernames:
        typer.echo("The user already exists")
        raise typer.Abort()
    else:
        existing_usernames.append(username)
        typer.echo(f"User created: {username}")


def send_new_notification(username: str) -> None:
    typer.echo(f"Notification sent to the new user: {username}")


def main(username: str) -> None:
    maybe_create_user(username)
    send_new_notification(username)


if __name__ == "__main__":
    typer.run(main)
