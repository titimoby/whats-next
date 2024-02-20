import config
import gitlab
from rich.console import Console
from rich.table import Table

# Function to get todos from GitLab
def get_gitlab_todos():
    # Initialize GitLab
    gl = gitlab.Gitlab(url=config.gitlab_server, private_token=config.gitlab_token)

    # Get todos
    todos = gl.todos.list(project_id=config.gitlab_project_id, all=True)
    return [todo.attributes for todo in todos]


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
