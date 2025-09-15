import csv
import statistics
def analizador_csv():
    archivo = input("Ruta del archivo CSV: ")
    try:
        with open(archivo, newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            datos = list(lector)
        if not datos:
            print("El archivo está vacío.")
            return
        columnas = datos[0].keys()
        columnas_numericas = []
        for col in columnas:
            try:
                float(datos[0][col])
                columnas_numericas.append(col)
            except ValueError:
                pass
        print("\dato--- ESTADÍSTICAS DEL CSV ---")
        for col in columnas_numericas:
            valores = [float(fila[col]) for fila in datos if fila[col].strip() != ""]
            if valores:
                print(f"\nColumna: {col}")
                print(f"  Total de valores: {len(valores)}")
                print(f"  Promedio: {statistics.mean(valores):.2f}")
                print(f"  Mínimo: {min(valores)}")
                print(f"  Máximo: {max(valores)}")
            else:
                print(f"\nColumna: {col} (sin datos numéricos)")
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
if __name__ == "__main__":
    analizador_csv()
