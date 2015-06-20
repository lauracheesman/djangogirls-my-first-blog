*Test Markdown*

# Start Env
python3 -m venv myvenv
# working with virtual environment
source myvenv/bin/activate

# creates django project
django-admin startproject mysite .

# run webserver
python manage.py runserver
http://127.0.0.1:8000/

# create Database
python manage.py makemigrations <APP>
python manage.py migrate <APP>

#Creating an application
python manage.py startapp blog
python manage.py startapp race
