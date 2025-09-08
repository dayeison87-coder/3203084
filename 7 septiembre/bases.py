import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="trabajo",
    user="postgres",
    password="1234",
    port=5432
)
print(conn)
print("Conexión exitosa a la base de datos")

cursor = conn.cursor()
cursor.execute(" CREATE TABLE USUARIO ( ID SERIAL PRIMARY KEY, NOMBRE VARCHAR(50), EDAD INT, CIUDAD VARCHAR(50))") 

conn.commit()
cursor.close()
conn.close()

