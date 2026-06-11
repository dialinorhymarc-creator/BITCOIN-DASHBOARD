import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="crypto_db",
        user="postgres",
        password="admin123"
    )