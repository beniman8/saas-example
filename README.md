# saas-setup

=======

# journal

A Saas Journal

- [x] dependencies
- [x] Django set up
- [x] configuration via python decouple
- [x] Configure web server Gunicorn for heroku using Profile different for Linode
- [x] testing
- [ ] Continuous Integration
- [x] pre-commit
- [x] Django modeling
- [ ] Heroku / Linode set up
- [x] User/auth account app
- [x] Django allauth setings and settup
- [x] Finish TODO for allauth
- [x] email/password
- [x] Email templates
- [x] setup console email backend
- [x] add templates for login/logout
- [x] Django management command

## setup on for windows

```
virtualenv venv
pip install -r requirements-dev.txt -r requirements.txt
django-admin startproject core .
py manage.py runserver
```

if you want to use Makefile on windows you need to dowload it in choco from your shell

run shell and you should be able to install it and have the ability to use it in cmd, shell etc..

```
choco install make

```
