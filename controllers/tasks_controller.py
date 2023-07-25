from flask import Flask, render_template, redirect, request, Blueprint
from app import db
from models import Task, User

tasks_blueprint = Blueprint("tasks", __name__)

@tasks_blueprint.route("/tasks")
def tasks():
	tasks = Task.query.all()
	return render_template('tasks/index.jinja', tasks=tasks)