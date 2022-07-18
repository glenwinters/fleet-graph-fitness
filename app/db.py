import psycopg2

DB_NAME = "fitness"
DB_USER = "postgres"
DB_PASSWORD = "fitness"
DB_HOST="localhost"
DB_PORT = 5011

connection = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, port=DB_PORT)


