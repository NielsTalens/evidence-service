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

## 1.  Create the db localy. - Test BDB

- In PgAdmin: select server and right click: Create > Database.

## 2. Create tables in the db


`python setup/create-evidence-table.py`
`python setup/create-control-table.py`

## 3. Create testdata

- Create test controls

INSERT INTO controls (control_id, control_description, control_value)
VALUES
('1748-E', 'A control to prevent data loss', 1),
('3333-X', 'Multi factor authentication ON', 1),
('1748-G', 'Security code scans scheduled ON', 1),
('MAN-1X', 'Dependency check scheduled ON', 1);


- Create test evidence

INSERT INTO evidence (rule_description, control_id, retrieved_value)
VALUES
('Retrieved rule description', 'A control to see the authentication rules', 1),
('A control to prevent data loss', '1748-E', 1),
('A control to prevent vulnerabilities', '1748-G', 1),
('A control to prevent dependencies', 'MAN-1X', 2);

## 4. Run the evidence service

`python evidence-serivce.py`

## 5. See all mapped controls

`python get-mapped-controls.py`

## 6. Get the frontend up and running

In the frontend directory:
## 7. Install dependencies

$ pip install psycopg2-binary
$ pip install flask-sqlalchemy
$ pip install Flask-Migrate

## 8. Run the frontend

- Run the following command in the frontend directory: `FLASK_APP=app.py FLASK_ENV=development flask run`
- Visit [localhost](http://127.0.0.1:5000/)


## Snippets

- Find the control-evidence map:

SELECT evidence.id, controls.id, evidence.retrieved_value, controls.control_value FROM evidence INNER JOIN controls ON evidence.control_id=controls.control_id;
