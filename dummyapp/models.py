from django.db import models

# Create your models here.
import pymysql
conn = pymysql.connect(
    host='testdb.cf8asksiuwjo.us-west-1.rds.amazonaws.com',
    port=3306,
    user='admin',
    password='rainbow77',
    db='Team0402'
)

def newfunc():
    cursor = conn.cursor()
    cursor.execute('select * from TestDBTable ')
    varNew = cursor.fetchall()
    return varNew

def newfuncDelete():
    cursor = conn.cursor()
    cursor.execute('delete from TestDBTable ')
    varNewOne = cursor.fetchall()
    return varNewOne