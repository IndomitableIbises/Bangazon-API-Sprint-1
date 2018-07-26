#!/bin/bash

find . -path "/$1/migrations/*.py" -not -name "__init__.py" -delete; #deletes all of the .py files in the migrations directory except for the __init__.py file.
find . -path "/$1/migrations/*.pyc"  -delete; #deletes all of the .pyc files in the migrations directory.
rm db.sqlite3; #deletes the database file.
python manage.py makemigrations $1; #creates the migration and the new db file.
python manage.py migrate; #runs the migration.
python manage.py $2 #runs the custom command to generate fake data and populate your tables with it