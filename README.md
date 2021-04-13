# evidence-service

## Pre requisites

- Python & pip
- Postgres
- PgAdmin
- Psycopg
## Setup

- Install Postgres:
`brew install postgresql`
- [Install PgAdmin](https://www.pgadmin.org/download/pgadmin-4-macos/)
- [Setup Postgres](https://docs.bitnami.com/installer/apps/canvaslms/administration/configure-pgadmin/)

- install Psycopg locally (connect to Postgres)
`pip install psycopg2-binary`

[Alternative ways to install](https://www.psycopg.org/docs/install.html)

## 1.  Create the db localy

- In PgAdmin: select server and right click: Create > Database.

## 2. Create a table in the db

Run the following script: `python create-table.py`

## 3. Run the script

`python evidence-serivce.py`