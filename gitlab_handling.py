import config
import gitlab

# Function to get todos from GitLab
def get_gitlab_todos():
    # Initialize GitLab
    gl = gitlab.Gitlab(url=config.gitlab_server, private_token=config.gitlab_token)

    # Get todos
    todos = gl.todos.list(project_id=config.gitlab_project_id, all=True)
    return [todo.attributes for todo in todos]
