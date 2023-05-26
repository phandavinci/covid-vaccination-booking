
## BookMyVaX

![LOGO](readmefiles/logo.jpg)

A web application for covid vaccination booking



## Badges


![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/phandavinci/DevRev)
## Installation


For Environmental installation of packages
```bash
  pip3 install pipenv
```

To environmentally install pip environment 

```bash
  pipenv install django pytz
```

## Folder Structure

<details open>
    <summary>devrev: master file which contains all the settings</summary>
    <ul>
        <li> _pycache_: cache files</li>
        <li>migrations: db cache and migraions</li>
        <li>_init_.py: normal init py file</li>
        <li>asgi.py: It exposes the ASGI callable as a module-level variable named ``application``</li>
        <li>settings.py: Django settings for devrev project. Generated by 'django-admin startproject' using Django 4.2.1.</li>
        <li>urls.py: URL configuration for devrev project.</li>
        <li>wsgi.py: It exposes the WSGI callable as a module-level variable named ``application``</li>
    </ul>
</details>
<details open>
    <summary>templates: frontend folders</summary>
    <ul>
        <li>admin: contains simple UI of admin</li>
        <li>user: contains simple UI of user</li>
    </ul>
</details>

<details open>
    <summary>user folder: backend of user</summary>
    <ul>
        <li> _pycache_: cache files</li>
        <li>migrations: db cache and migraions</li>
        <li>_init_.py: normal init py file</li>
        <li>admin.py: enable admin control of db</li>
        <li>apps.py: app configuration</li>
        <li>models.py: for db managing, creating, etc</li>
        <li>urls.py: for defining the urls for each backend folder</li>
        <li>views.py: contains backend for each apps</li>
        <li>test.py: for testing the server</li>
    </ul>
</details>

<details open>
    <summary>admin folder: backend of admin</summary>
    <ul>
        <li> _pycache_: cache files</li>
        <li>migrations: db cache and migraions</li>
        <li>_init_.py: normal init py file</li>
        <li>admin.py: enable admin control of db</li>
        <li>apps.py: app configuration</li>
        <li>models.py: for db managing, creating, etc</li>
        <li>urls.py: for defining the urls for each backend folder</li>
        <li>views.py: contains backend for each apps</li>
        <li>test.py: for testing the server</li>
    </ul>
</details>

<details open>
    <summary>centers folder: backend for centers(db of centers & some computing functions)</summary>
    <ul>
        <li> _pycache_: cache files</li>
        <li>migrations: db cache and migraions</li>
        <li>_init_.py: normal init py file</li>
        <li>admin.py: enable admin control of db</li>
        <li>apps.py: app configuration</li>
        <li>models.py: for db managing, creating, etc</li>
        <li>urls.py: for defining the urls for each backend folder</li>
        <li>views.py: contains backend for each apps</li>
        <li>test.py: for testing the server</li>
    </ul>
</details>
    - dbsqlite: SQL Database

## Run Locally
Clone the project

```bash
  git clone https://github.com/phandavinci/devrev.git
```

Go to the project directory

```bash
  cd your/path/to/project/devrev-main
```

Start the server in terminal or commandline

```bash
  pipenv python manage.py runserver
```

Link for homepage:http://127.0.0.1:8000/ or http://localhost:8000

## Testing Accounts

### - For user

- Mobileno: 9555595555
- Password: test

### - For Admin

- Username: admin 
- Password: admin
### For Database(Admin page login: http://127.0.0.1:8000/admin)
- Username: abishek
- password: abi123abi

## Acknowledgements
 - Django
 - Python v3.10
 - SQLite3

  
## Database Structure

![DatabaseStructureImage](readmefiles/models.png)

## Tests done 
`For Users:`
- Do they able to log in and register properly?
- Does the name of the user show correctly on the homepage?
- Do they able to search centres?
- Do they able to book a centre?
- Is vacancy showing?
- Is Booked alert showing?
- Does the vacancy limit of 10 bookings per day work?
- Do they able to log out properly?

`For Admin:`
- Does admin login and register work fine?
- Does the name of the admin show correctly on the homepage?
- Does the admin able to see all the centres on the homepage?
- Does admin search a particular centre using its I'd?
- Does the admin able to remove a centre?
- Does the admin able to view the whole list of entries by the user and their info, particularly for a centre?
- Does the admin able to add centre?
- Does the admin able to log out?