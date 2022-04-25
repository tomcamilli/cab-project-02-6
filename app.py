#! /usr/bin/python3

"""
This is an example Flask | Python | Psycopg2 | PostgreSQL
application that connects to the 7dbs database from Chapter 2 of
_Seven Databases in Seven Weeks Second Edition_
by Luc Perkins with Eric Redmond and Jim R. Wilson.
The CSC 315 Virtual Machine is assumed.

John DeGood
degoodj@tcnj.edu
The College of New Jersey
Spring 2020

----

One-Time Installation

You must perform this one-time installation in the CSC 315 VM:

# install python pip and psycopg2 packages
sudo pacman -Syu
sudo pacman -S python-pip python-psycopg2

# install flask
pip install flask

----

Usage

To run the Flask application, simply execute:

export FLASK_APP=app.py 
flask run
# then browse to http://127.0.0.1:5000/

----

References

Flask documentation:  
https://flask.palletsprojects.com/  

Psycopg documentation:
https://www.psycopg.org/

This example code is derived from:
https://www.postgresqltutorial.com/postgresql-python/
https://scoutapm.com/blog/python-flask-tutorial-getting-started-with-flask
https://www.geeksforgeeks.org/python-using-for-loop-in-flask/
"""

import psycopg2
from config import config
from flask import Flask, render_template, request

def dateTranslate(soe, year, month):
	startday = '01'
	endday = '01'
	m = 0;
	if month == 'January':
		endday = '31'
		m = '01'
	elif month == 'February':
		endday = '28'
		m = '02'
	elif month == 'March':
		endday = '31'
		m = '03'
	elif month == 'April':
		endday = '30'
		m = '04'
	elif month == 'May':
		endday = '31'
		m = '05'
	elif month == 'June':
		endday = '30'
		m = '06'
	elif month == 'July':
		endday = '31'
		m = '07'
	elif month == 'August':
		endday = '31'
		m = '08'
	elif month == 'September':
		endday = '30'
		m = '09'
	elif month == 'October':
		endday = '31'
		m = '10'
	elif month == 'November':
		endday = '30'
		m = '11'
	elif month == 'December':
		endday = '31'
		m = '12'
	
	if soe == 's':
		return '%s-%s-%s' % (year, m, startday)
	elif soe == 'e':
		return '%s-%s-%s' % (year, m, endday)
	

# Connect to the PostgreSQL database server
def connect(query):
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the %s database...' % (params['database']))
        conn = psycopg2.connect(**params)
        print('Connected.')
      
        # create a cursor
        cur = conn.cursor()
        
        # execute a query using fetchall()
        cur.execute(query)
        rows = cur.fetchall()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    # return the query result from fetchall()
    return rows
 
# app.py
app = Flask(__name__)


# serve form web page
@app.route("/")
def form():
	return render_template('eD-form.html')

@app.route("/building-handler")
def building_handle():#r
	buildinglist = connect('SELECT BuildingName FROM buildings;')
	return render_template('eD-form.html', buildinglist=buildinglist)

# handle venue POST and serve result web page
@app.route('/venue-handler', methods=['POST'])
def building_handler():
	buildinglist = connect('SELECT BuildingName FROM buildings;')
	return render_template('eD-form.html', buildinglist=buildinglist)

def venue_handler():
	rows = connect('SELECT MeterName, MeterType FROM meters WHERE MeterType = \'' + request.form['MeterTypeDrop'] + '\';')
	return render_template('my-result.html', rows=rows)


# handle query POST and serve result web page
@app.route('/query-handler', methods=['POST'])
def query_handler():
    rows = connect(request.form['query'])
    return render_template('my-result.html', rows=rows)

@app.route('/meter-cost-handler', methods=['POST'])
def meter_cost_handler():
	y = request.form['year']
	m = request.form['month']
	rows = connect('SELECT MeterName, Cost, Usage, StartDate FROM meters NATURAL JOIN costs WHERE MeterType = \'' + request.form['metertype'] + '\' AND StartDate >= \'' + dateTranslate('s',y,m) + '\' AND StartDate <= \'' + dateTranslate('e',y,m) +'\';')
	heads = ['meter', 'cost', 'usage', 'date']
	return render_template('my-result.html', rows=rows, heads=heads)

if __name__ == '__main__':
    app.run(debug = True)
