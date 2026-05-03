from flask import Blueprint, render_template, request, flash, url_for, redirect, session, g

from todor.auth import login_required

from .models import Todo, User
from todor import db

bp = Blueprint('todo', __name__, url_prefix='/todo')

 

@bp.route('/list')
@login_required
def index():
        todos = Todo.query.filter_by(created_by=g.user.id).all()
        return render_template('todo/index.html')

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        todo = Todo(g.user.id, title, description)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/create.html')

def get_todo(id):
     todo = Todo.query.get_or_404(id)
     return todo

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
     todo = get_todo(id)
     if request.method == 'POST':
        todo.title = request.form['title']
        todo.description = request.form['description']
        todo.state = True if request.form.get('state') == 'on' else False

        db.session.commit()
        return redirect(url_for('todo.index'))
     return render_template('todo/update.html', todo = todo)

@bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
     todo = get_todo(id)
     db.session.delete(todo)
     db.session.commit()
     return redirect(url_for('todo.index'))
