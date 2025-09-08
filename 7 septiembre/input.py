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

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
ciudad = input("Ingrese su ciudad: ")
cursor.execute("INSERT INTO USUARIO (nombre, edad, ciudad) VALUES (%s, %s, %s)", (nombre, edad, ciudad))
conn.commit()
cursor.close()
conn.close()