from flask import Flask
import sqlite3
import json

# Run server
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World'

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
        return res

@app.route('/getpatient')
def get_patient(patientID):
    with sqlite3.connect('KVDB.db') as conn:
        # Construct the query
        select_query = "SELECT * FROM patients WHERE patientID=" + patientID

        # Get pointer to db
        db_cursor = conn.cursor()

        # Pass the query to DB
        db_cursor.execute(select_query)

        res = db_cursor.fetchone()

        # Get results
        return json.dumps(res)

@app.route('/insertpatient')
def post_patient(patientName, parentName, phoneNumber, meData, aeData):
    with sqlite3.connect('KVDB.db') as conn:
        insert_query = "INSERT INTO patients(patientName, parentName, phoneNumber, meData, aeData) VALUES(" + patientName + parentName + phoneNumber + meData + aeData + ")"
        
        db_cursor = conn.cursor()

        db_cursor.execute(insert_query)

        res = db_cursor.fetchall()

        # Get results
        return res

if __name__ == '__main__':
    app.run(port=5000)