# evidence-service

## Pre requisites

- Python & pip
- Postgres
- PgAdmin
- Psycopg
## Setup

- Install Postgres: `brew install postgresql`
- Install PgAdmin: `brew install --cask pgadmin4`
- [Setup local Postgres server](https://docs.bitnami.com/installer/apps/canvaslms/administration/configure-pgadmin/)
- Install Psycopg: `pip install psycopg2-binary`

## 1.  Create the db localy. - Test BDB2

- In PgAdmin: select server and right click: Create > Database.

## 2. Create tables in the db

`python setup/ca_populate.py`

## 3. Create testdata

`python setup/ca_schema.py`
- Create test controls

## 4. Run the evidence service - Skip for now

ToDo: connect to Azure api to retrieve control data.
`python evidence-serivce.py`

## 5. Get the frontend up and running

In the frontend directory:
## 6. Install dependencies

$ pip install psycopg2-binary
$ pip install flask-sqlalchemy
$ pip install Flask-Migrate

## 7. Run the frontend

- Run the following command in the frontend directory: `FLASK_APP=app.py FLASK_ENV=development flask run`
- Visit [localhost](http://127.0.0.1:5000/)

