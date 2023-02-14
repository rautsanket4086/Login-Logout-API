import pymysql
from app import app
from db_config import mysql
from flask import jsonify, request, session
# from werkzeug import check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt()


@app.route('/')
def home():
	if 'username' in session:
		username = session['username']
		return jsonify({'message' : 'You are already logged in', 'username' : username})
	else:
		resp = jsonify({'message' : 'Unauthorized'})
		resp.status_code = 401
		return resp

@app.route('/login', methods=['POST'])
def login():
    conn = None		
    cursor = None
    try:
        _json = request.get_json()
        _username = _json.get('username')
        _password = _json.get('password')
        if not all([_username, _password]):
            return jsonify({'message': 'Bad Request - Invalid Credentials'}), 400
        conn = mysql.connector.connect(user='choice', password='choice@123',
                              host='127.0.0.1', database='user_details',   auth_plugin='mysql_native_password')		
        cursor = conn.cursor()
        print("Hello World")
        cursor.execute("SELECT * FROM user WHERE username=%s", (_username,))
        row = cursor.fetchone()
        if not row:
            return jsonify({'message': 'Bad Request - Invalid username'}), 400

        if check_password_hash(row[2], _password):
            return jsonify({'message': 'Bad Request - Invalid password'}), 400

        session['username'] = row[1]
        return jsonify({'message': 'You are logged in successfully'})

    except Exception as e:
        print(e)
        return jsonify({'message': 'An error occurred during the login process'}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username', None)
	return jsonify({'message' : 'You successfully logged out'})
		
if __name__ == "__main__":
    app.run(port = 5001)

