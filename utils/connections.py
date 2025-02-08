import oracledb
import psycopg2
import colorama
from configs.config import *

def connect_to_oracle(dsn, database, host, port):
    try:
        connection = oracledb.connect(dsn)
        if connection:
            print(f"Database: {database} on host: {host} and port: {port} has been connected")
        oracle_cursor = connection.cursor()
        return oracle_cursor
    except Exception as e:
        print(f"Error: {e}")

def connect_to_postgres(dbname, host, user, password, port):
    try:
        connection = psycopg2.connect(
            dbname=dbname, 
            user=user, 
            password=password, 
            host=host, 
            port=port)
        if connection:
            print(f"Database: {dbname} on host: {host} and port: {port} has been connected")
        postgres_cursor = connection.cursor()
        return postgres_cursor
    except Exception as e:
        print(f"Error: {e}")