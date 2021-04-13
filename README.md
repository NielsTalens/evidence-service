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

## 1.  Create the db localy

- In PgAdmin: select server and right click: Create > Database.

## 2. Create a table in the db

`python create-table.py`

## 3. Run the evidence service

`python evidence-serivce.py`