from datetime import datetime
from sqlalchemy import select
from forms import Create_todo


def filter_todos_status(Todo, request):
    query = Todo.query
    todo_status = request.args.get("todo_status")
    sort = request.args.get("sort_order_status")

    if todo_status:
        query = query.filter(Todo.done == False)
    if sort:
        query = query.order_by(Todo.date.asc())
    else:
        query = query.order_by(Todo.date.desc())


    return query.all()



def create_todo(db, Todo):
    form = Create_todo()

    if form.task.data and form.subject.data:
        new_todo = Todo(
            task=form.task.data,
            subject = form.subject.data,
            done=False,
            date=datetime.utcnow()
        )
        db.session.add(new_todo)
        db.session.commit()



def change_status_todo(db, Todo, todo_id):
    todo = db.session.execute(select(Todo).where(Todo.id == todo_id)).scalar()

    if todo:
            todo.done = not todo.done
            db.session.commit()




def delete_todos(db, Todo, todo_id):
    todo = db.session.execute(select(Todo).where(Todo.id == todo_id)).scalar()

    if todo:
            db.session.delete(todo)
            db.session.commit()