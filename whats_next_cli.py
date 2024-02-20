from rich.console import Console
from rich.table import Table
from gitlab_handling import get_gitlab_todos


def show_todo_list():
    """
    Show the todo items
    """
    todos = get_gitlab_todos()
    table = Table(title="Todo List")

    table.add_column("Creation Date", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Description", justify="right", style="green")

    for item in todos:
        table.add_row(
            item["target"]["created_at"], item["target"]["title"], item["body"]
        )

    console = Console()
    console.print(table)
