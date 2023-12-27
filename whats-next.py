import gitlab
import os
from flask import Flask, render_template
import config

# Initialize Flask app
app = Flask(__name__)


# Function to get todos from GitLab
def get_gitlab_todos():
    # Initialize GitLab
    gl = gitlab.Gitlab(url=config.gitlab_server, private_token=config.gitlab_token)

    # Get project
    project = gl.projects.get(config.gitlab_project_id)

    # Get todos
    todos = gl.todos.list(all=True)
    return [todo.attributes for todo in todos]


# Route to display todos
@app.route("/")
def index():
    todos = get_gitlab_todos()
    return render_template("todos.html", todos=todos)


if __name__ == "__main__":
    app.run(debug=True)
