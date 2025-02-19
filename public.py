from flask import *
from database import *
import uuid
# from comparison import *

public=Blueprint('public',__name__)

@public.route('/')
def homepage():
	# q="select * from login"
	# res=select(q)
	# print(res)
	# print(type(res))
	return render_template('homepage.html')

@public.route('/login',methods=['get','post'])
def login():

	if 'submit' in request.form:
		uname=request.form['uname']
		passs=request.form['pwd']
		q="SELECT * FROM `login` WHERE username='%s' AND `password`='%s'"%(uname,passs)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['user_type']=='admin':
				flash('WELCOME TO ADMIN HOME')
				return redirect(url_for('admin.adminhome'))
			if res[0]['user_type']=='hospital':
				q="SELECT * FROM hospitals WHERE `login_id`='%s'"%(res[0]['login_id'])
				res2=select(q)
				session['hid']=res2[0]['hospital_id']
				session
				flash('WELCOME TO HOSPITAL HOME')
				return redirect(url_for('hospital.hospitalhome'))
				
			if res[0]['user_type']=='doctor':
				q="SELECT * FROM doctor WHERE `login_id`='%s'"%(res[0]['login_id'])
				res2=select(q)
				session['did']=res2[0]['doctor_id']
				flash('WELCOME TO DOCTOR HOME')
				return	redirect(url_for('doctor.doctor_home'))

			if res[0]['user_type']=='patient':
				q="SELECT * FROM patients WHERE `login_id`='%s'"%(res[0]['login_id'])
				rr=select(q)
				session['pid']=rr[0]['patient_id']
				flash('WELCOME TO PATIENT HOME')
				return	redirect(url_for('patient.patient_home'))

			if res[0]['user_type']=='pharmacy':
				q="SELECT * FROM pharmacy WHERE `login_id`='%s'"%(res[0]['login_id'])
				rr=select(q)
				session['phid']=rr[0]['pharmacy_id']
				flash('WELCOME TO PHARMACY HOME')
				return	redirect(url_for('pharmacy.pharmacyhome'))
		else:
			flash("Username Or password Is Wrong")
	return render_template('login.html')