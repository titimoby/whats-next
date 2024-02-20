from flask import Flask, render_template
from gitlab_handling import get_gitlab_todos

# Initialize Flask app
webapp = Flask(__name__)

# Route to display todos
@webapp.route("/")
def index():
    todos = get_gitlab_todos()
    return render_template("todos.html", todos=todos)


def launch():
    webapp.run()


if __name__ == "__main__":
    webapp.run(debug=True)
