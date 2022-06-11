# Web application - SurveyApply!
Running the Web-App:

Assumes a working Python 3 installation (with python=python3 and pip=pip3).

(1) Run the code below to install the dependencies.

>$ pip install Flask
>$ pip install psycopg2


(2) Database Initialization

1. create database in pgadmin4
2. run database.sql in pgadmin4
3. run insert_database.sql in pgadmin4
4. in app.py - insert "dbname='DBNAME' user='USER' host='localhost' password='PASSWORD'"


(3) Run Web-App

>$ python app.py


# May 12, 2022 - June 12, 2022 DEVELOPMENT AND KEY DATES

(Background on how this code came into existence.)


May 12, 2022 
Initially we wanted to make a web-app for statistics and information about footballers in ingland. 
We made a power point, ERD and had a good idea of the app.

May 26, 2022 
We've decided to drop our initial web-app idea, and gone for another. 
Our new idea is to create an web-app where yo inter yor age, height, shoesize 
and then you will recieve an email with your own submission details and the average height and shoesize and how many participants have submited.

We have created the webpage for data collection, and a redirected webpage for successful data collection.

June 2, 2022 

we have our database up and running and the connection between web-app and database is on. 

june 7, 2022
We have finished our web-app so that it looks nice and added an button to return to homepage if you are sitting with a friend to submit together.

June 8, 2022
We have created 'database.sql' and 'insert_database.sql' with some fictive data for our web app. 

June 11, 2022
we make a ERD of our database. 

June 12, 2022 The project-due-date
 
