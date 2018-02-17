# Internship Assignment
### Problem 2 (Expiry Remainder)
#### First things to be installed to run this project is 
######1. Python
######2. Django

####For Database i have used sqlite

####Firstly migrate the database ,
######python manage.py makemigrations
######python manage.py migrate

####Run the server
###### python manage.py runserver

##### No need of superuser till now
###### User can add truck data by filling following data-
######1. Truck Number - i.e. MH92BU1234 (maximum letter is 10)
######2. Insurance Expiry date,Fitness Expiry date, Pollution Expiry date in YYYY-MM-DD format
####then save the data by clicking submit.
#### You will be notified if any truck's insurance or fitness or pollution will be going to expired.
#### You will get remainder at 7,15,30 days before the expiry and once you marked read then notification get move to past notification.
#### You can also see past notification by clicking button on notification page.
#### Suppose you get remainder for 30 day remaining and you marked remainder as seen though you will get remainder again before 15 day of expiry and same will happen for 7 day before expiry.
#### For renew the insurance or fitness or pollution you have to add that truck again and old data will automatically get deleted