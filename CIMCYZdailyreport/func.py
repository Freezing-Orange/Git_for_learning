import pymysql
from pymysql import cursors
def mysqlConnect(userName,userPassword):
    db=pymysql.connect(host="localhost",user=userName,password=userPassword,database="dutytest")
    cursors=db.cursor()
    return cursors