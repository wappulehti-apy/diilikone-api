# Diilikone API

## Requirements
- Python 3.4
- virtualenvwrapper
- autoenv
- postgresql

## Development environment setup
### Create virtualenv
```shell
$ mkvirtualenv --python=$(which python3.5) diilikone-api
```
### Install python dependecies
```shell
$ pip install -r requirements-dev.txt
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
### Add required environment variables
```shell
echo 'workon diilikone-api' >> .env
echo 'export FLASK_APP=$(pwd)/autoapp.py' >> .env
echo 'export DEBUG=1' >> .env
```

### Run tests
```shell
py.test
```
### Start development server
```shell
flask run
```
### Start Shell
```shell
flask konch
```


## Additional resources
- https://exploreflask.com/
- http://flask.pocoo.org/
