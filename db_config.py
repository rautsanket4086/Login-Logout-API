from app import app
# import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb


# from MySQLdb import mysqldb
# from flask_MySQLdb import MySQL
# from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
# from flask_mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'choice'
app.config['MYSQL_DATABASE_PASSWORD'] = 'choice@123'
app.config['MYSQL_DATABASE_DB'] = 'user_details'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql = MySQL(app)

mysql.init_app(app)
