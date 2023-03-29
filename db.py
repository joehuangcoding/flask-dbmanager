import mysql.connector
from mysql.connector import FieldType
import click
from flask import current_app
from flask import g

dbconn = None
connection = None

def get_db():
    global dbconn
    global connection
    if connection is None or (connection is not None and connection.is_connected() == 0) : 
        connection = mysql.connector.connect(user=current_app.config["DB_USER"], \
        password=current_app.config["DB_PASS"], host=current_app.config["DB_HOST"], \
        database=current_app.config["DB_NAME"], autocommit=True)
        dbconn = connection.cursor()
    g.connection = connection
    g.db = dbconn
    g.db.row_factory = connection.cursor(dictionary=True)
    return g.db

