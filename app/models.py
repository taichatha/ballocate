from app import db
from datetime import datetime

class State(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)

	def __repr__(self):
		return '<State %r>' % (self.name)

class Court(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)
	address = db.Column(db.String(128))
	lat = db.Column(db.Float)
	lng = db.Column(db.Float)
	attendances = db.relationship('Attendance', backref='court', lazy='dynamic')
	
	def __repr__(self):
		return '<Court: %r>' % (self.name)

class Attendance(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	people = db.Column(db.Integer, default=0)
	date = db.Column(db.DateTime, default=datetime.now().date())
	court_id = db.Column(db.Integer, db.ForeignKey('court.id'))

	def __repr__(self):
		return '<%r>' % (self.people)