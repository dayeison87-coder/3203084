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
cursor.execute("""
    INSERT INTO USUARIO(nombre, edad, ciudad) VALUES
    ('Carlos', '25', 'Madrid'),
    ('Ana', '15', 'Barcelona'),
    ('Luis', '30', 'Valencia'),
    ('María', '22', 'Sevilla'),
    ('Pedro', '28', 'Zaragoza'),
    ('Laura', '19', 'Málaga'),
    ('Jorge', '35', 'Murcia'),
    ('Camila', '27', 'Palma'),
    ('Andrés', '40', 'Bilbao'),
    ('Valentina', '18', 'Alicante');
""")
conn.commit()
cursor.close()
conn.close()