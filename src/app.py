from enum import unique
from re import I
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
import psycopg2
import numpy as np

app = Flask(__name__)


try:
    conn=psycopg2.connect("dbname='height_collector' user='postgres' host='localhost' password='pilealle15'")
    print("Welcome to height_collector")
except:
    print ("I am unable to connect to the database.")

cur = conn.cursor()
try:
    cur.execute("""SELECT * from data1""")
except:
    print ("I can't drop our test database!")

rows = cur.fetchall()
print ("\nRows: \n")
for row in rows:
    print ("   ", row)


#AVERAGE HEIGHT
cur = conn.cursor()
sql = """
    SELECT AVG(height_) 
    FROM Data1 
    """
cur.execute(sql)

res = cur.fetchall()
print ("\n avg_height: \n")
for r in res:
    print(r[0])

#AVERAGE SHOESIZE
cur = conn.cursor()
sql = """
    SELECT AVG(shoesize) 
    FROM Data1 
    """
cur.execute(sql)
size = cur.fetchall()
print ("\n avg_shoesize: \n")
for s in size:
    print(s[0])


def insert_Customers(name, surname, email, height, age, shoesize):
    cur = conn.cursor()
    sql = """
    INSERT INTO data1(name_, surname_, email_, height_, age_, shoesize)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    res = cur.execute(sql, (name, surname, email, height, age, shoesize))
    print(res)
    conn.commit()
    cur.close()



# Creating a route that connects to the index server
@app.route("/")
def index():
    return render_template("index.html")

# Create a route that connects from the index to the sucess page and sends an email to the customer
@app.route("/success", methods=["POST"])
def success():
        if request.method=="POST":
            name = request.form["name_name"]
            surname = request.form["surname_name"]
            email = request.form["email_name"]
            height = request.form["height_name"]
            age = request.form["age_name"]
            shoesize = request.form["shoesize_name"]
            avg_height = r[0]
            avg_shoesize = s[0]
            insert_Customers(name, surname, email, height, age, shoesize)
            print("foo")
            send_email(name, surname, email, height, age, shoesize, avg_height, avg_shoesize)
            return render_template("success.html")
        return render_template('index.html', text="The email you're trying to use is not valid. Please try again.")


if __name__ == "__main__":
    app.debug = True
    app.run()