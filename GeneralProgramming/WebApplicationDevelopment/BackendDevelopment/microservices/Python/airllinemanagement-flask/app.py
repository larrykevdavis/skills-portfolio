from flask import Flask, jsonify, request,render_template,redirect,url_for,session
import pymysql.cursors
import csv

# start the definitions of the flask app
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'


#getting the total number of staff
def get_total_staff(connection):
	with connection.cursor() as cursor:
		sql = "SELECT COUNT(*) as total_staff FROM staff"
		cursor.execute(sql)
		result = cursor.fetchone()
		return result

#getting all the staff
def get_all_staff(connection):
	with connection.cursor() as cursor:
		sql = "SELECT * FROM staff"
		cursor.execute(sql)
		result = cursor.fetchall()
		return result


#getting the total number of students
def get_total_student(connection):
	with connection.cursor() as cursor:
		sql = "SELECT COUNT(*) as total_student FROM student"
		cursor.execute(sql)
		result = cursor.fetchone()
		return result

#getting all the students
def get_all_student(connection):
	with connection.cursor() as cursor:
		sql = "SELECT * FROM student"
		cursor.execute(sql)
		result = cursor.fetchall()
		return result


#getting the total number of airport workers
def get_total_airportworkers(connection):
	with connection.cursor() as cursor:
		sql = "SELECT COUNT(*) as total_workers FROM airport_worker"
		cursor.execute(sql)
		result = cursor.fetchone()
		return result

#getting all the airport workers
def get_all_airportworkers(connection):
	with connection.cursor() as cursor:
		sql = "SELECT * FROM airport_worker"
		cursor.execute(sql)
		result = cursor.fetchall()
		return result

#getting the total number of users
def get_total_users(connection):
	with connection.cursor() as cursor:
		sql = "SELECT COUNT(*) as total_users FROM users"
		cursor.execute(sql)
		result = cursor.fetchone()
		return result

#getting all the users
def get_all_users(connection):
	with connection.cursor() as cursor:
		sql = "SELECT * FROM users"
		cursor.execute(sql)
		result = cursor.fetchall()
		return result

#updating all users with no accounts
def update_unregistered_users(connection):
	with connection.cursor() as cursor:
		sql = "SELECT * FROM student"
		cursor.execute(sql)
		result = cursor.fetchall()

		session['staff_list']=[]
		session['student_list']=[]
		session['worker_list']=[]

		for student_dict in result:
			studentid=student_dict['student_id']
			sql = "SELECT * FROM users WHERE user_id=%s"
			values=(studentid,)
			cursor.execute(sql,values)

			if cursor.rowcount==0:
				session['student_list'].append(student_dict)


		sql = "SELECT * FROM staff"
		cursor.execute(sql)
		result = cursor.fetchall()

		for staff_dict in result:
			staffid=staff_dict['staff_id']
			sql = "SELECT * FROM users WHERE user_id=%s"
			values=(staffid,)
			cursor.execute(sql,values)

			if cursor.rowcount==0:
				session['staff_list'].append(staff_dict)


		sql = "SELECT * FROM airport_worker"
		cursor.execute(sql)
		result = cursor.fetchall()

		for worker_dict in result:
			workerid=worker_dict['worker_id']
			sql = "SELECT * FROM users WHERE user_id=%s"
			values=(workerid,)
			cursor.execute(sql,values)

			if cursor.rowcount==0:
				session['worker_list'].append(worker_dict)




# Admin Dashboard Functionality
###################################################
@app.route('/admin-dashboard/',methods=['GET'])
def admin_view():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	total_staff_dict=get_total_staff(connection)
	total_student_dict=get_total_student(connection)
	total_airport_dict=get_total_airportworkers(connection)
	total_users_dict=get_total_users(connection)
	return render_template('admin.html',total_staff=total_staff_dict['total_staff'],total_student=total_student_dict['total_student'],total_workers=total_airport_dict['total_workers'],total_users=total_users_dict['total_users'])


#### -- STAFF FUNCTIONALITY -- ########
@app.route('/add-staff/',methods=['POST'])
def add_staff():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form
		staffid=int(form['staffid'])
		name=form['name']
		email=form['email']
		age=int(form['age'])
		location=form['location']
		phonenumber=int(form['phonenumber'])
		print(staffid)
		sql_statement = "INSERT INTO staff (staff_id,staff_name,staff_age,staff_location,staff_email,staff_phonenumber) VALUES (%s, %s,%s,%s,%s,%s)"
		values = (staffid,name,age,location,email,phonenumber)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['res']="success"
		else:
			session['res']="error"

		connection.commit()

	return redirect(url_for('staff_information_view'))

@app.route('/update-staff/',methods=['POST'])
def update_staff():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form
		staffid=int(form['staffid'])
		name=form['name']
		email=form['email']
		age=int(form['age'])
		location=form['location']
		phonenumber=int(form['phonenumber'])
		print(staffid)
		sql_statement = "UPDATE staff SET staff_name=%s,staff_age=%s,staff_location=%s,staff_email=%s,staff_phonenumber=%s WHERE staff_id=%s"
		values = (name,age,location,email,phonenumber,staffid)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['updateres']="success"
		else:
			session['updateres']="error"

		connection.commit()

	return redirect(url_for('staff_information_view'))

@app.route('/delete-staff/<id>',methods=['GET'])
def delete_staff(id):
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		sql_statement = "DELETE FROM staff WHERE staff_id=%s"
		values = (id,)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['del']="success"
		else:
			session['del']="error"

		connection.commit()

	return redirect(url_for('staff_information_view'))

#### -- STUDENT FUNCTIONALITY -- ########
@app.route('/add-student/',methods=['POST'])
def add_student():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form
		studentid=int(form['studentid'])
		name=form['name']
		email=form['email']
		age=int(form['age'])
		phonenumber=int(form['phonenumber'])

		sql_statement = "INSERT INTO student (student_id,student_name,student_email,student_age,student_phonenumber) VALUES (%s, %s,%s,%s,%s)"
		values = (studentid,name,email,age,phonenumber)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['res']="success"
		else:
			session['res']="error"

		connection.commit()

	return redirect(url_for('student_information_view'))

@app.route('/update-student/',methods=['POST'])
def update_student():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form
		studentid=int(form['studentid'])
		name=form['name']
		email=form['email']
		age=int(form['age'])
		phonenumber=int(form['phonenumber'])

		sql_statement = "UPDATE student SET student_name=%s,student_email=%s,student_age=%s,student_phonenumber=%s WHERE student_id=%s"
		values = (name,email,age,phonenumber,studentid)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['updateres']="success"
		else:
			session['updateres']="error"

		connection.commit()

	return redirect(url_for('student_information_view'))

@app.route('/delete-student/<id>',methods=['GET'])
def delete_student(id):
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		sql_statement = "DELETE FROM student WHERE student_id=%s"
		values = (id,)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['del']="success"
		else:
			session['del']="error"

		connection.commit()

	return redirect(url_for('student_information_view'))

#### -- AIRLINE WORKER FUNCTIONALITY -- ########
@app.route('/add-worker/',methods=['POST'])
def add_worker():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form
		workerid=int(form['workerid'])
		name=form['name']
		email=form['email']
		phonenumber=int(form['phonenumber'])

		sql_statement = "INSERT INTO airport_worker (worker_id,worker_name,worker_email,worker_phonenumber) VALUES (%s, %s,%s,%s)"
		values = (workerid,name,email,phonenumber)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['res']="success"
		else:
			session['res']="error"

		connection.commit()

	return redirect(url_for('airport_staff_information_view'))

@app.route('/update-worker/',methods=['POST'])
def update_worker():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form
		workerid=int(form['workerid'])
		name=form['name']
		email=form['email']
		phonenumber=int(form['phonenumber'])

		sql_statement = "UPDATE airport_worker SET worker_name=%s,worker_email=%s,worker_phonenumber=%s WHERE worker_id=%s"
		values = (name,email,phonenumber,workerid)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['updateres']="success"
		else:
			session['updateres']="error"

		connection.commit()

	return redirect(url_for('airport_staff_information_view'))

@app.route('/delete-worker/<id>',methods=['GET'])
def delete_worker(id):
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		sql_statement = "DELETE FROM airport_worker WHERE worker_id=%s"
		values = (id,)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['del']="success"
		else:
			session['del']="error"

		connection.commit()

	return redirect(url_for('airport_staff_information_view'))


#### -- USER FUNCTIONALITY -- ########
@app.route('/add-user/',methods=['POST'])
def add_user_info():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form
		userid=int(form['userid'])
		email=form['email']
		password=form['password']
		category=form['category']

		sql_statement = "INSERT INTO users (user_id,username,password,category) VALUES (%s, %s,%s,%s)"

		values = (userid,email,password,category)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['res']="success"
		else:
			session['res']="error"

		connection.commit()

	return redirect(url_for('users_information_view'))

@app.route('/update-user/',methods=['POST'])
def update_user():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form
		userid=int(form['userid'])
		email=form['email']
		password=form['password']
		category=form['category']

		sql_statement = "UPDATE users SET username=%s,password=%s WHERE user_id=%s"
		values = (email,password,userid)
		cursor.execute(sql_statement, values)

		session['updateres']="success"
	
		connection.commit()

	return redirect(url_for('users_information_view'))

@app.route('/delete-user/<id>',methods=['GET'])
def delete_user(id):
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		sql_statement = "DELETE FROM users WHERE user_id=%s"
		values = (id,)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['del']="success"
		else:
			session['del']="error"

		connection.commit()

	return redirect(url_for('users_information_view'))

###################################################

###################################################
@app.route('/staff-information/',methods=['GET'])
def staff_information_view():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	staff_list=get_all_staff(connection)
	return render_template('staff.html',staff_list=staff_list)

###################################################


###################################################
@app.route('/student-information/',methods=['GET'])
def student_information_view():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	student_list=get_all_student(connection)
	return render_template('students.html',student_list=student_list)

###################################################

###################################################
@app.route('/airport-staff-information/',methods=['GET'])
def airport_staff_information_view():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	workers_list=get_all_airportworkers(connection)
	return render_template('airport-workers.html',workers_list=workers_list)

###################################################

###################################################
@app.route('/users-information/',methods=['GET'])
def users_information_view():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	update_unregistered_users(connection)
	users_list=get_all_users(connection)
	return render_template('users.html',users_list=users_list)

###################################################


# Airport Dashboard Functionality
###################################################
#getting the total number of airlines
def get_total_airlines(connection):
	with connection.cursor() as cursor:
		sql = "SELECT COUNT(*) as total_airlines FROM airlines"
		cursor.execute(sql)
		result = cursor.fetchone()
		return result

#getting all the airlines
def get_all_airlines(connection):
	with connection.cursor() as cursor:
		sql = "SELECT * FROM airlines"
		cursor.execute(sql)
		result = cursor.fetchall()
		return result


#getting the total number of aircrafts
def get_total_aircrafts(connection):
	with connection.cursor() as cursor:
		sql = "SELECT COUNT(*) as total_aircrafts FROM aircraft"
		cursor.execute(sql)
		result = cursor.fetchone()
		return result

#getting all the aircrafts
def get_all_aircrafts(connection):
	with connection.cursor() as cursor:
		sql = "SELECT * FROM aircraft LEFT JOIN airlines ON aircraft.airline_id=airlines.airline_id"
		cursor.execute(sql)
		result = cursor.fetchall()
		return result


#getting the total number of routes
def get_total_routes(connection):
	with connection.cursor() as cursor:
		sql = "SELECT COUNT(*) as total_routes FROM routes"
		cursor.execute(sql)
		result = cursor.fetchone()
		return result

#getting all the routes
def get_all_routes(connection):
	with connection.cursor() as cursor:
		sql = "SELECT * FROM routes"
		cursor.execute(sql)
		result = cursor.fetchall()
		return result


#getting the total number of flights
def get_total_flights(connection):
	with connection.cursor() as cursor:
		sql = "SELECT COUNT(*) as total_flights FROM flights"
		cursor.execute(sql)
		result = cursor.fetchone()
		return result

#getting all the flights
def get_all_flights(connection):
	with connection.cursor() as cursor:
		sql = "SELECT * FROM flights LEFT JOIN aircraft ON flights.aircraft_id=aircraft.aircraft_id LEFT JOIN airlines ON aircraft.airline_id=airlines.airline_id LEFT JOIN routes on flights.route_id=routes.route_id"
		cursor.execute(sql)
		result = cursor.fetchall()
		return result

#getting all the non booked flights
def get_all_non_booked_flights(connection):
	with connection.cursor() as cursor:
		sql = "SELECT * FROM flights LEFT JOIN aircraft ON flights.aircraft_id=aircraft.aircraft_id LEFT JOIN airlines ON aircraft.airline_id=airlines.airline_id LEFT JOIN routes on flights.route_id=routes.route_id"
		cursor.execute(sql)
		result = cursor.fetchall()
		newresult=[]
		for flight_dict in result:
			flight_id=flight_dict['flight_id']
			user_id=session['user_id']
			sql = "SELECT * FROM bookings WHERE flight_id=%s and user_id=%s"
			values=(flight_id,user_id)
			cursor.execute(sql,values)
			if cursor.rowcount>0:
				pass
			else:
				newresult.append(flight_dict)

		return newresult

#getting the total number of bookings
def get_total_bookings(connection):
	with connection.cursor() as cursor:
		sql = "SELECT COUNT(*) as total_bookings FROM bookings"
		cursor.execute(sql)
		result = cursor.fetchone()
		return result

def get_bookings_by_id(connection,id):
	with connection.cursor() as cursor:
		sql = "SELECT * FROM bookings WHERE booking_id=%s"	
		values=(id,)
		cursor.execute(sql,values)
		result = cursor.fetchone()
		return result

def get_user_bookings(connection,id):
	with connection.cursor() as cursor:
		sql = "SELECT * FROM bookings LEFT JOIN users on users.user_id=bookings.user_id LEFT JOIN flights ON flights.flight_id=bookings.flight_id LEFT JOIN routes ON routes.route_id=flights.route_id LEFT JOIN aircraft ON aircraft.aircraft_id=flights.aircraft_id LEFT JOIN airlines ON airlines.airline_id=aircraft.airline_id WHERE bookings.user_id=%s"
	
		values=(id,)
		cursor.execute(sql,values)
		result = cursor.fetchall()
		return result

#getting all the bookings
def get_all_bookings(connection):
	with connection.cursor() as cursor:
		sql = "SELECT * FROM bookings LEFT JOIN users on users.user_id=bookings.user_id LEFT JOIN flights ON flights.flight_id=bookings.flight_id LEFT JOIN routes ON routes.route_id=flights.route_id LEFT JOIN aircraft ON aircraft.aircraft_id=flights.aircraft_id LEFT JOIN airlines ON airlines.airline_id=aircraft.airline_id"
		cursor.execute(sql)
		result = cursor.fetchall()

		newresult=[]

		for booking_dict in result:
			category=""
			user_id=booking_dict['user_id']
			idtype=""
			newdict={}

			if booking_dict['category']=="staff":
				category="staff"
				idtype="staff_id"
			else:
				category="student"
				idtype="student_id"

			sql = "SELECT * FROM %s WHERE %s=%s"%(category,idtype,user_id)
			
			cursor.execute(sql)
			result = cursor.fetchone()

			if category=="staff":
				result["passenger_name"]=result["staff_name"]
			else:
				result["passenger_name"]=result["student_name"]

			newdict.update(booking_dict)
			newdict.update(result)
			newresult.append(newdict)

		return newresult

#getting the total number of passengers
def get_total_passengers(connection):
	with connection.cursor() as cursor:
		sql = "SELECT COUNT(DISTINCT user_id) as total_passengers FROM bookings"
		cursor.execute(sql)
		result = cursor.fetchone()
		return result


@app.route('/airport-dashboard/',methods=['GET'])
def airport_view():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	total_airline_dict=get_total_airlines(connection)
	total_aircraft_dict=get_total_aircrafts(connection)
	total_route_dict=get_total_routes(connection)
	total_flight_dict=get_total_flights(connection)
	total_booking_dict=get_total_bookings(connection)
	total_passenger_dict=get_total_passengers(connection)
	booking_list=get_all_bookings(connection)

	return render_template('airport.html',total_airlines=total_airline_dict['total_airlines'],total_aircrafts=total_aircraft_dict['total_aircrafts'],total_routes=total_route_dict['total_routes'],total_flights=total_flight_dict['total_flights'],total_bookings=total_booking_dict['total_bookings'],total_passengers=total_passenger_dict['total_passengers'],booking_list=booking_list)


@app.route('/export-to-csv/',methods=['GET'])
def export_to_csv():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	booking_list=get_all_bookings(connection)
	csv_list=[]
	for booking_dict in booking_list:
		newdict={}
		newdict['passenger_name']=booking_dict['passenger_name']
		newdict['airline_name']=booking_dict['airline_name']
		newdict['aircraft_name']=booking_dict['aircraft_name']
		newdict['traveller_type']=booking_dict['traveller_type']
		newdict['class']=booking_dict['class']
		newdict['flight_date']=booking_dict['flight_date'].strftime('%m/%d/%Y')
		newdict['flight_time']=str(booking_dict['flight_time'])   
		newdict['route_name']=booking_dict['route_name']   
		newdict['route_type']=booking_dict['route_type']   
		newdict['review_title']=booking_dict['review_title'] 
		newdict['review']=booking_dict['review']  
		newdict['rating']=booking_dict['rating']  
		newdict['value_for_money']=booking_dict['value_for_money']
		newdict['recommended']=booking_dict['recommended']
		csv_list.append(newdict)

	keys = csv_list[0].keys()
	with open('newcastle_airport_dataset.csv', 'w', newline='') as output_file:
		dict_writer = csv.DictWriter(output_file, keys)
		dict_writer.writeheader()
		dict_writer.writerows(csv_list)

	session['export']="success"

	return redirect(url_for('airport_view'))

@app.route('/airline-information/',methods=['GET'])
def airline_view():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	airline_list=get_all_airlines(connection)
	return render_template('airlines.html',airline_list=airline_list)


#### -- AIRLINE INFORMATION FUNCTIONALITY -- #######
@app.route('/add-airline/',methods=['POST'])
def add_airline_info():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form

		name=form['name']
		country=form['country']

		sql_statement = "INSERT INTO airlines (airline_name,country_of_origin) VALUES (%s, %s)"

		values = (name,country)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['res']="success"
		else:
			session['res']="error"

		connection.commit()

	return redirect(url_for('airline_view'))

@app.route('/update-airline/',methods=['POST'])
def update_airline():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form
		airlineid=int(form['airlineid'])

		name=form['name']
		country=form['country']

		sql_statement = "UPDATE airlines SET airline_name=%s,country_of_origin=%s WHERE airline_id=%s"
		values = (name,country,airlineid)
		cursor.execute(sql_statement, values)

		session['updateres']="success"
	
		connection.commit()

	return redirect(url_for('airline_view'))

@app.route('/delete-airline/<id>',methods=['GET'])
def delete_airline(id):
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		sql_statement = "DELETE FROM airlines WHERE airline_id=%s"
		values = (id,)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['del']="success"
		else:
			session['del']="error"

		connection.commit()

	return redirect(url_for('airline_view'))

###################################################


@app.route('/aircraft-information/',methods=['GET'])
def aircraft_view():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	airline_list=get_all_airlines(connection)
	aircraft_list=get_all_aircrafts(connection)
	return render_template('aircrafts.html',airline_list=airline_list,aircraft_list=aircraft_list)
#### -- AIRCRAFT INFORMATION FUNCTIONALITY -- #######
@app.route('/add-aircraft/',methods=['POST'])
def add_aircraft_info():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form

		airlineid=form['airlineid']
		name=form['name']
		first=form['first']
		business=form['business']
		economy=form['economy']

		sql_statement = "INSERT INTO aircraft (airline_id,aircraft_name,first_class_capacity,business_class_capacity,economy_class_capacity) VALUES (%s,%s,%s,%s,%s)"

		values = (airlineid,name,first,business,economy)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['res']="success"
		else:
			session['res']="error"

		connection.commit()

	return redirect(url_for('aircraft_view'))

@app.route('/update-aircraft/',methods=['POST'])
def update_aircraft():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form
		aircraftid=int(form['airlineid'])

		airlineid=int(form['airlineid'])
		name=form['name']
		first=form['first']
		business=form['business']
		economy=form['economy']

		sql_statement = "UPDATE aircraft SET airline_id=%s,aircraft_name=%s,first_class_capacity=%s,business_class_capacity=%s,economy_class_capacity=%s WHERE aircraft_id=%s"
		values = (airlineid,name,first,business,economy,aircraftid)
		cursor.execute(sql_statement, values)

		session['updateres']="success"
	
		connection.commit()

	return redirect(url_for('aircraft_view'))

@app.route('/delete-aircraft/<id>',methods=['GET'])
def delete_aircraft(id):
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		sql_statement = "DELETE FROM aircraft WHERE aircraft_id=%s"
		values = (id,)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['del']="success"
		else:
			session['del']="error"

		connection.commit()

	return redirect(url_for('aircraft_view'))

###################################################

@app.route('/route-information/',methods=['GET'])
def route_view():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	route_list=get_all_routes(connection)
	return render_template('routes.html',route_list=route_list)

#### -- ROUTE INFORMATION FUNCTIONALITY -- #######
@app.route('/add-route/',methods=['POST'])
def add_route_info():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form

		name=form['name']
		rtype=form['rtype']
		source=form['source']
		destination=form['destination']

		sql_statement = "INSERT INTO routes (route_name,route_type,route_source,route_destination) VALUES (%s,%s,%s,%s)"

		values = (name,rtype,source,destination)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['res']="success"
		else:
			session['res']="error"

		connection.commit()

	return redirect(url_for('route_view'))

@app.route('/update-route/',methods=['POST'])
def update_route():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form
		routeid=int(form['routeid'])

		name=form['name']
		rtype=form['rtype']
		source=form['source']
		destination=form['destination']

		sql_statement = "UPDATE routes SET route_name=%s,route_type=%s,route_source=%s,route_destination=%s WHERE route_id=%s"
		values = (name,rtype,source,destination,routeid)
		cursor.execute(sql_statement, values)

		session['updateres']="success"
	
		connection.commit()

	return redirect(url_for('route_view'))

@app.route('/delete-route/<id>',methods=['GET'])
def delete_route(id):
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		sql_statement = "DELETE FROM routes WHERE route_id=%s"
		values = (id,)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['del']="success"
		else:
			session['del']="error"

		connection.commit()

	return redirect(url_for('route_view'))

###################################################

@app.route('/flight-information/',methods=['GET'])
def flight_view():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	flight_list=get_all_flights(connection)
	aircraft_list=get_all_aircrafts(connection)
	route_list=get_all_routes(connection)
	return render_template('flights.html',flight_list=flight_list,aircraft_list=aircraft_list,route_list=route_list)

#### -- FLIGHT INFORMATION FUNCTIONALITY -- #######
@app.route('/add-flight/',methods=['POST'])
def add_flight_info():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form

		aircraftid=form['aircraftid']
		routeid=form['routeid']
		date=form['date']
		time=form['time']

		sql_statement = "INSERT INTO flights (aircraft_id,route_id,flight_date,flight_time) VALUES (%s,%s,%s,%s)"

		values = (aircraftid,routeid,date,time)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['res']="success"
		else:
			session['res']="error"

		connection.commit()

	return redirect(url_for('flight_view'))

@app.route('/update-flight/',methods=['POST'])
def update_flight():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form
		flightid=int(form['flightid'])

		aircraftid=form['aircraftid']
		routeid=form['routeid']
		date=form['date']
		time=form['time']

		sql_statement = "UPDATE flights SET aircraft_id=%s,route_id=%s,flight_date=%s,flight_time=%s WHERE flight_id=%s"
		values = (aircraftid,routeid,date,time,flightid)
		cursor.execute(sql_statement, values)

		session['updateres']="success"
	
		connection.commit()

	return redirect(url_for('flight_view'))

@app.route('/delete-flight/<id>',methods=['GET'])
def delete_flight(id):
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		sql_statement = "DELETE FROM flights WHERE flight_id=%s"
		values = (id,)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['del']="success"
		else:
			session['del']="error"

		connection.commit()

	return redirect(url_for('flight_view'))

###################################################


@app.route('/booking-information/',methods=['GET'])
def booking_view():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	booking_list=get_all_bookings(connection)
	return render_template('bookings.html',booking_list=booking_list)

@app.route('/view-reviews/',methods=['POST'])
def reviews_view():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	form=request.form
	bookingid=form['id']
	review_dict=get_bookings_by_id(connection,bookingid)
	return render_template('reviews.html',review_dict=review_dict)


##########################################################
@app.route('/book-flight/',methods=['GET'])
def book_flight_view():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	non_booked=get_all_non_booked_flights(connection)
	return render_template('book.html',non_booked=non_booked)

#### -- FLIGHT BOOKING INFORMATION FUNCTIONALITY -- #######
@app.route('/add-flight-booking',methods=['POST'])
def add_flight_booking_info():
	result=""

	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form

		user_id=form['user_id']
		flight_id=form['flight_id']
		tclass=form['class']
		traveller=form['traveller']

		sql_statement = "INSERT INTO bookings (user_id,flight_id,class,traveller_type) VALUES (%s,%s,%s,%s)"

		values = (user_id,flight_id,tclass,traveller)
		cursor.execute(sql_statement, values)

		if cursor.rowcount>0:
			session['res']="success"
		else:
			session['res']="error"

		connection.commit()

	return redirect(url_for('book_flight_view'))



###################################################

@app.route('/booking-history/',methods=['GET'])
def booking_history_view():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	book_list=get_user_bookings(connection,session['user_id'])
	return render_template('booking_history.html',book_list=book_list)

@app.route('/reviews/',methods=['GET'])
def review_view():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	return render_template('add-review.html')


@app.route('/',methods=['GET'])
def login_view():
	return render_template('login.html')

@app.route('/login/',methods=['POST'])
def login():
	connection = pymysql.connect(host='localhost',user='root',password='',database='airline',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	with connection.cursor() as cursor:
		form=request.form
			
		email=form['email']
		password=form['password']
			
		sql_statement = "SELECT * FROM users WHERE username=%s and password=%s"
		values = (email,password)
		cursor.execute(sql_statement, values)
		result=cursor.fetchone()
		urlfor=""

		if cursor.rowcount>0:
			session['user_id']=result['user_id']
			if result['category']=='staff' or result['category']=='student' :
				urlfor='book_flight_view'
			elif result['category']=='worker':
				urlfor='airport_view'
			elif result['category']=='admin':
				urlfor='admin_view'
		else:
			session['login']='error'
			urlfor='login_view'

	return redirect(url_for(urlfor))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)