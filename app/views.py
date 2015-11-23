from app import app, db
from datetime import datetime
from flask import  jsonify, render_template, flash, redirect, request, url_for
from .forms import LocateForm
from .models import State, Court, Attendance
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
# from .parse import outdoor_courts, indoor_courts 
import json
import os
GoogleMaps(app)
#Will have to look for .org, .gov, .edu links 
#start with arlington links


def populate_form_choices(locate_form):
	states = State.query.all()
	state_names = []
	for state in states:
		state_names.append(state.name)
	state_choices = list(enumerate(state_names))
	locate_form.state_select_field.choices = state_choices


@app.route('/', methods =['GET'])
@app.route('/index', methods = ['GET'])
def index():
	#creating a map view
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "static/js", "courts.json")
	data = json.load(open(json_url))
	courts = Court.query.all()
	for i in courts:
		if(i.attendances.all()[len(i.attendances.all())-1].date.date() != datetime.today().date()):
			#create an attendance for today
			a = Attendance(court_id=i.id)
			db.session.add(a)
			db.session.commit()
	attendances = Attendance.query.all()
	today_attendances = [x for x in attendances if x.date.date()==datetime.today().date()]
	today = datetime.today().date()

	return render_template("index.html",
		title='Ballocate',
		data = data,
		courts = courts,
		today = today
		
		)

@app.route('/up/<attendance_id>')
def up(attendance_id):
	attendance = Attendance.query.get(attendance_id)
	attendance.people += 1
	db.session.commit()
	return jsonify(result = attendance.people)
	

@app.route('/down/<attendance_id>')
def down(attendance_id):
	attendance = Attendance.query.get(attendance_id)
	if(attendance.people >0):
		attendance.people -= 1
		db.session.commit()
	
	

	return jsonify(result=attendance.people)

@app.route('/data')
def data():
	courts = Court.query.all()
	return render_template("data.html",
		title='Data',
		courts = courts)

@app.route('/get_loc', methods = ['GET'])
def get_loc():
    lng = request.args.get('lng')
    lat = request.args.get('lat')
    return jsonify(lat=lat, lng = lng)