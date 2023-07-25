from flask import Flask, render_template, redirect, request, Blueprint
from app import db
from models import Task, User

tasks_blueprint = Blueprint("tasks", __name__)

@tasks_blueprint.route("/tasks")
def tasks():
	tasks = Task.query.all()
	return render_template('tasks/index.jinja', tasks=tasks)

@tasks_blueprint.route("/tasks/<id>")
def show_tasks(id):
	task = Task.query.get(id)
	return render_template("tasks/show.jinja", task=task)

@tasks_blueprint.route("/tasks/new")
def add_task():
	users = User.query.all()
	return render_template("tasks/new.jinja", users=users)

@tasks_blueprint.route("/tasks", methods=['POST'])
def create_task():
	description = request.form['description']
	user_id = request.form['user_id']
	duration = request.form['duration']
	completed = 'completed' in request.form

	task = Task(description=description, user_id=user_id, duration=duration, completed=completed)

	db.session.add(task)
	db.session.commit()
	return redirect('/tasks')

@tasks_blueprint.route("/tasks/<id>/edit")
def edit_task(id):
	users = User.query.all()
	task = Task.query.get(id)
	return render_template('tasks/edit.jinja', task=task, users=users)

@tasks_blueprint.route("/tasks/<id>", methods=["POST"])
def update_task(id):
	description = request.form['description']
	user_id = request.form['user_id']
	duration = request.form['duration']
	completed = 'completed' in request.form
	
	task = Task.query.get(id)
	task.description = description
	task.user_id = user_id
	task.duration = duration
	task.completed = completed

	db.session.commit()
	return redirect('/tasks')