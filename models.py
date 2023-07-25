from app import db

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True) # primary key will auto-increment id
	first_name = db.Column(db.String(64))
	last_name = db.Column(db.String(64))
	tasks = db.relationship('Task', backref='user') # backref creates on the task a user property so you can do task.user

	def __repr__(self):
		return f'<User {self.id}: {self.first_name} {self.last_name}>'

class Task(db.Model):
	__tablename__ = "tasks"
	id = db.Column(db.Integer, primary_key=True) # primary key will auto-increment id
	description = db.Column(db.Text())
	duration = db.Column(db.Integer)
	completed = db.Column(db.Boolean, default=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id')) # table_name.primary_key_column

	def __repr__(self):
		return f'<Task {self.id}: {self.description}>'