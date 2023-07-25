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

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True) # primary key will auto-increment id
	first_name = db.Column(db.String(64))
	last_name = db.Column(db.String(64))
	tasks = db.relationship('Task', backref='user') # backref creates on the task a user property so you can do task.user

	def __repr__(self):
		return f'<User {self.id}: {self.first_name} {self.last_name}>'

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True) # primary key will auto-increment id
	description = db.Column(db.Text())
	duration = db.Column(db.Integer)
	completed = db.Column(db.Boolean, default=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # table_name.primary_key_column

	def __repr__(self):
		return f'<Task {self.id}: {self.description}>'

@app.route("/")
def hello_world():
	return "Hello, World"