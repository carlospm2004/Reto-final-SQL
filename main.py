import os
import psycopg

url = os.getenv("DATABASE_URL")

try:
    with psycopg.connect(url) as connection:
        with connection.cursor() as cur:
            cur.execute(
                "INSERT INTO series (titulo, anio_estreno, n_temporadas) VALUES (%s, %s, %s)",
                ("Dark", 2017, 3),
            )

            cur.execute("SELECT * FROM series;")
            for fila in cur.fetchall():
                print(fila)

except Exception as e:
    print("Error:", e)
    raise