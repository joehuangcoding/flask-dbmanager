from flask import Blueprint
from flask import flash
from flask import render_template
from flask import request
from flask import url_for
from db import get_db
from datetime import datetime

bp = Blueprint("dbmanager", __name__, url_prefix="/dbmanager")

@bp.route("/", methods = ["GET"])
def dbmanager():
    table_list = []
    now = datetime.now()
    db = get_db();
    sql = '''
        show Tables;
        '''
    nowtime = 'SELECT NOW();'
    db.execute(sql)
    db_result = db.fetchall()
    db_cols = [desc[0] for desc in db.description]
    # table_list.append(Table(db_cols, db_result))
    table_names = db_result
    db.execute(nowtime)
    db_result1 = db.fetchall()
    for table_name in db_result:
        table_list.append(get_the_table(table_name[0]))
    return render_template("dbmanager.html", table_list=table_list, table_names=table_names, now=now, db_result1=db_result1)

@bp.route("/", methods = ["POST"])
def dbupdate():
    json = request.get_json()
    for update in json:
        key_info = update['key'].split("-")
        column_to_update = key_info[0]
        table_to_update = key_info[1]
        primary_key = key_info[2]
        primary_key_id = key_info[3]
        new_value = update['new']
        update_the_table(table_to_update, column_to_update, new_value, primary_key, primary_key_id)
    return "db updated"

class Table:
    column_names = []
    data = []
    def __init__(self, column_names, data):
        self.column_names = column_names
        self.data = data

def get_the_table(table_name):
    db = get_db()
    sql = f"""select * from {table_name};"""
    db.execute(sql)
    db_result = db.fetchall()
    db_cols = [desc[0] for desc in db.description]
    return Table(db_cols, db_result)

def update_the_table(table, column, value, primary_key, primary_key_id): 
    db = get_db()
    sql = f"""Update {table} SET {table}.{column} = '{value}' WHERE {primary_key} = {primary_key_id};"""
    db.execute(sql)
