import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="phonebook_db",
        user="postgres",
        password="12345678"  
    )

# тест
conn = connect()
print("Connected!")
conn.close()