# Script Análisis de ventas
# mediante un archivo datos.csv en el subdirectorio datos/ con los datos:
# - producto ->         ID
# - fecha de venta ->   sales_date
# - cantidad vendida -> sales_amount
# 
# se realiza el análisis de:
# - ventas totales
# - producto mas vendido
# - ventas por mes
#
# exportando grafico en el subdirectorio resultados/

# importación de bibliotecas
import csv, os

# Generando ruta base (raíz/scrips)
BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Ruta del archivo datos.csv
RUTA_CSV = os.path.join(BASE_DIR, "datos", "datos.csv")

def leer_csv(ruta:str) -> list[dict]:
# lee un archivo csv y retorna una lista de directorios.
    if not os.path.exists(ruta):
        raise FileNotFoundError(f'No se encontró el archivo: {ruta}')
    
    registros=[]

    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            registros.append(dict(fila))

    return registros

#
if __name__=="__main__":
    print(f'Análisis de ventas {RUTA_CSV}')
    try:
        datos = leer_csv(RUTA_CSV)
        print(datos)
    except FileNotFoundError as e:
        print(f'ERROR {e}')
    except Exception as e:
        print(f'Error inesperado {e} {type(e)}')