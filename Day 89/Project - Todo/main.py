import os
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from database import database
from functions import filter_todos_status,create_todo,change_status_todo, delete_todos
from dotenv import load_dotenv
load_dotenv()
from forms import Create_todo

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Bootstrap5(app)
db, Todo = database(app)




@app.route("/", methods=["GET"])
def home():
    create_todo_form = Create_todo()
    todos = filter_todos_status(Todo, request)


    return render_template(
        'todos.html',
        todos=todos,
        create_todo_form=create_todo_form
    )





@app.route("/create", methods=["POST"])
def create():

    create_todo(db, Todo)
    return redirect(url_for("home"))





@app.route("/status/<int:todo_id>", methods=["POST"])
def status(todo_id):

    change_status_todo(db, Todo, todo_id)
    return redirect(url_for("home", **request.args))





@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete_todo(todo_id):

    delete_todos(db, Todo, todo_id)
    return redirect(url_for("home", **request.args))



if __name__ == '__main__':
    app.run(debug=True)