import typer
import config
import gitlab
from rich.pretty import pprint
from rich.console import Console
from rich.table import Table

app = typer.Typer()


@app.command("list")
def todo_list():
    import whats_next_cli as cli

    cli.show_todo_list()


@app.command("web")
def todo_list_web():
    import whats_next_web as web

    web.launch()


if __name__ == "__main__":
    app()
