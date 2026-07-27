#!/bin/bash

echo "Creating file Structure for project"
echo "_______________________________________________________"
echo "Making Directory"
echo "_______________________________________________________"

appname="app"

#creating App and it's sub Directories
mkdir $appname
mkdir $appname/db
mkdir $appname/core
mkdir $appname/api

#Test Directory
mkdir tests

#log files
mkdir logs

echo ""
echo "_______________________________________________________"
echo "sub Directory"
echo "_______________________________________________________"

# creating multiple folder at once (AS List) 

#For app
for files in __init__.py main.py models.py schemas.py logging_config.py
	do
		touch "$appname/$files"
		echo "created $files"
	done

#For db
for files in __init__.py session.py models.py
	do
		touch "$appname/db/$files"
		echo "created $files"
	done

#for core
for files in __init__.py config.py secureity.py dependencies.py
	do 
		touch "$appname/core/$files"
		echo "created $files"
	done

#for api
for files in __init__.py user.py
	do
		touch "$appname/api/$files"
		echo "created $files"
	done

#Testing files
echo "_______________________________________________________"
echo "Creating Test files"
echo "_______________________________________________________"

#as simple
touch "tests/__init.py"
touch "tests/test_users.py"

echo "test files created."

# celery Directories
echo "_______________________________________________________"
echo "Creating Celery directory"
echo "_______________________________________________________"

echo ""
mkdir "celery"
for files in __init__.py celery_app.py tasks.py
	do
		touch "celery/$files"
		echo "created celery/$files"
	done
echo "Celery folder created."
echo ""


#other additional files
echo "_______________________________________________________"
echo "Creating other files"
echo "_______________________________________________________"

for files in requirements.txt README.md Dockerfile docker-compose.yml .dockerignore .gitignore .env  
do
	touch "$files"
	echo "$files created."
done

# adding some files in .gitignore file
echo ".env
__pycache__
logs
.pyc
" >> .gitignore


echo ""
echo "_______________________________________________________"
echo "Creating and Initializing Virtual Environment"
echo "_______________________________________________________"
echo ""

python -m venv .venv
echo "Virtual Environment created."

echo "Activating Virtual Environment"
source .venv/bin/activate
echo "Activated."
echo ""

echo "_______________________________________________________"
echo "Installing lib and packages"
echo "_______________________________________________________"

for lib in fastapi redis celery postgres psycopg2-binary asyncpg sqlalchemy
	do 
		echo "installing $lib"
		pip install $lib
		echo "installed."
		echo ""
	done
echo "Installed Libraries"
echo "___________________________________________________________"

echo "updating requirements.txt file"
pip freeze > requirements.txt
echo "Updated."
echo ""

echo "_______________________________________________________"
echo "File Structure Completed."
echo "_______________________________________________________"

echo "File Structure"
tree
