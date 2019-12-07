from flask import Flask, request
from flask_cors import CORS
import sqlite3
import json

# Run server
app = Flask(__name__)
CORS(app)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/authorizelogin')
def authorize():
    with sqlite3.connect('KVDB.db') as conn:
        userID = request.args.get('userID')
        select_query = "SELECT password FROM users WHERE userID='" + userID + "'"
        db_cursor = conn.cursor()
        db_cursor.execute(select_query)
        return db_cursor.fetchone()[0]

@app.route('/getalldata')
def get_patients():
    with sqlite3.connect('KVDB.db') as conn:
        # Construct the query
        select_query = "SELECT * FROM patients"

        # Get pointer to db
        db_cursor = conn.cursor()

        # Pass the query to DB
        db_cursor.execute(select_query)

        res = db_cursor.fetchall()

        # Get results
        return json.dumps(res)

@app.route('/getpatientbyid')
def get_patient():
    with sqlite3.connect('KVDB.db') as conn:
        patientID = request.args.get('patientID')
        # Construct the query
        select_query = "SELECT * FROM patients WHERE patientID=" + patientID
        
        # Get pointer to db
        db_cursor = conn.cursor()

        # Pass the query to DB
        db_cursor.execute(select_query)

        return json.dumps(db_cursor.fetchone())

@app.route('/getpatientbyname')
def get_patientByName():
    with sqlite3.connect('KVDB.db') as conn:
        patientName = request.args.get('patientName')
        # Construct the query
        select_query = "SELECT * FROM patients WHERE patientName='" + patientName + "'"

        # Get pointer to db
        db_cursor = conn.cursor()

        # Pass the query to DB
        db_cursor.execute(select_query)

        return json.dumps(db_cursor.fetchone())

@app.route('/insertpatient')
def post_patient():
    with sqlite3.connect('KVDB.db') as conn:
        patientName = request.args.get('patientName')
        parentName = request.args.get('parentName')
        phoneNumber = request.args.get('phoneNumber')
        aeData = request.args.get('aeData')
        meData = request.args.get('meData')

        insert_query = "INSERT INTO patients(patientName, parentName, phoneNumber, aeData, meData) VALUES('" + patientName + "', '" +  parentName + "', " + phoneNumber + ", " + aeData + ", '" + meData + "')"
        print(insert_query)
        db_cursor = conn.cursor()

        db_cursor.execute(insert_query)  

        return "OK"

if __name__ == '__main__':
    app.run(port=5000)
