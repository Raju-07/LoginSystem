## Login System

    Introduction:

    This project is is for  create the user Register and login System in asyncmode using JWT Authentication.

    OAuth will be integrated later on in this project. In this when the user Registered an account an email will be sent.

For Mail we're using google SMTP

## Tech Stacks

* Fastapi
* docker
* redis
* celery
* postgres

File Structure

```
LoginSystem
├── app
│   ├── api
│   │   ├── __init__.py
│   │   └── user.py
│   ├── core
│   │   ├── config.py
│   │   ├── dependencies.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── config.cpython-313.pyc
│   │   │   └── __init__.cpython-313.pyc
│   │   └── secureity.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── session.py
│   ├── __init__.py
│   ├── loggin_config.py
│   ├── main.py
│   ├── models.py
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   └── main.cpython-313.pyc
│   └── schemas.py
├── celery
│   ├── celery_app.py
│   ├── __init__.py
│   └── tasks.py
├── docker-compose.yml
├── Dockerfile
├── file-structure.sh
├── logs
├── README.md
├── requirements.txt
└── tests
    ├── __init.py
    └── test_users.py

10 directories, 28 files
```

## Colaboration

Hello, Everyone this Project include the jwt authentication if anyone want to integrated Authentication use this repo to integrated within your preject.

It'll help you to developed your application more fast and easy to build. save you time and you can make some changes accoding to your  need
