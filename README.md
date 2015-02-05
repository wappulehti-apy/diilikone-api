# Diilikone API

## Requirements
- Python 3.4
-- asdasd
- virtualenvwrapper
- postgresql

## Development environment setup
### Create virtualenv
```shell
$ mkvirtualenv --python=$(which python3.4) diilikone-api
```
### Install python dependecies
```shell
$ pip install -r requirements.txt
```
### Create development and testing databases
```shell
$ createdb diilikone
$ createdb diilikone_test
```
### Upgrade database tables
```shell
$ alembic upgrade head
```
### Run tests
```shell
py.test
```
### Start development server
```shell
python manage.py runserver
```


## Additional resources
- https://exploreflask.com/
- http://flask.pocoo.org/
