from configs.config import *
from utils.banner import banner
from utils.connections import connect_to_oracle, connect_to_postgres

def main():
    connect_to_oracle(oracle_dsn, oracle_database, oracle_host, oracle_port)
    connect_to_postgres(postgres_database, postgres_host, postgres_user, postgres_password, postgres_port)

if __name__ == "__main__":
    banner()
    main()