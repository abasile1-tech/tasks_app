from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os
from dotenv import load_dotenv

load_dotenv()
PASSWORD = os.getenv('PASSWORD')

app = Flask(__name__)
# for new project, change 'tasks_app' to db name
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:{PASSWORD}@localhost:5432/tasks_app"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controllers.tasks_controller import tasks_blueprint
app.register_blueprint(tasks_blueprint)

# @app.route("/")
# def hello_world():
# 	# delete all the rows
# 	Task.query.delete() # immediately delete
# 	User.query.delete()

# 	sky = User(first_name="Sky", last_name="Su")
# 	db.session.add(sky) # stage changes
# 	print("Sky before commit")
# 	print(sky)

# 	jason = User(first_name="Jason", last_name="Sweeney")
# 	db.session.add(jason) #stage changes
# 	db.session.commit() # commit
# 	print("Sky after commit")
# 	print(sky)

# 	# get all the users
# 	users = User.query.all()
# 	print("get all the users")
# 	print(users)

# 	# get a user by id
# 	found_user = User.query.get(jason.id)
# 	print(f"get user by id = {jason.id}")
# 	print(found_user)

# 	# create tasks
# 	task1 = Task(description="Survive this lesson", duration=120, user=sky)
# 	db.session.add(task1)

# 	task2 = Task(description="Survive the next lesson", duration=90, completed=True, user=jason)
# 	db.session.add(task2)

# 	db.session.commit()

# 	#get all the tasks
# 	all_tasks = Task.query.all()
# 	print("get all the tasks")
# 	print(all_tasks)

# 	print("jason's tasks")
# 	print(jason.tasks)

# 	print("tasks[0]'s user")
# 	print(all_tasks[0].user.first_name)

# 	# mark task1 as completed
# 	task1.completed = True
# 	db.session.commit()

# 	db.session.delete(task2)
# 	db.session.commit()

	# return render_template("tasks/index.jinja" all_tasks=Task.query.all())