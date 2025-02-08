from utils.connections import *

def get_oracle_tables():
    oracle_cursor = connect_to_oracle(oracle_dsn, oracle_database, oracle_host)
    oracle_cursor.execute(f"SELECT table_name FROM user_tables")
    tables = [table[0] for table in oracle_cursor.fetchall()]
    return tables
    