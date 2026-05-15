# Script Análisis de ventas
# mediante un archivo datos.csv en el subdirectorio datos/ con los datos:
# - producto ->         ID
# - fecha de venta ->   sales_date
# - cantidad vendida -> sales_amount
# 
# se realiza el análisis de:
# - ventas totales
# - ventas por mes
#
# exportando gráfico en el subdirectorio resultados/

# importación de bibliotecas
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg") # Renderizado sin pantalla
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# -----------------------Rutas---------------
# Generando ruta base (raíz/scrips)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Ruta del archivo datos.csv
RUTA_CSV = os.path.join(BASE_DIR, "datos", "datos.csv")

#Ruta resultado grafico_ventas.png
RUTA_GRAF = os.path.join(BASE_DIR, "resultados", "grafico_ventas.png")

# ----------- Colores -------------
COLOR_PRINCIPAL = "#4F81BD"
COLOR_ACENTO    = "#C0504D"
COLOR_FONDO     = "#F5F5F5"

#-----------------------------------
MESES = {
    1: "Enero", 2: "Febrero", 3: "Marzo",    4: "Abril",
    5: "Mayo",  6: "Junio",   7: "Julio",    8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}



def leer_csv(ruta:str) -> pd.DataFrame:
# lee un archivo csv y retorna una lista de directorios.
    if not os.path.exists(ruta):
        raise FileNotFoundError(f'No se encontró el archivo: {ruta}')
    
    registro = pd.read_csv(ruta, parse_dates=['sales_date'])
    registro['mes']= registro['sales_date'].dt.month
    registro['nombre_mes'] = registro['mes'].map(MESES)

    return registro

def reporte_ventas_totales(datos: pd.DataFrame) -> None:

    total = datos['sales_amount'].sum()
    # promedio = sum(datos['sales_amount'] / len(datos['sales_amount']))
    # usando pandas
    promedio = datos['sales_amount'].mean()
    maximo = datos['sales_amount'].max()
    minimo = datos['sales_amount'].min()
    dias = len(datos)
    dia_max = datos.loc[datos['sales_amount'].idxmax(), 'sales_date'].strftime("%d/%m/%Y")
    dia_min = datos.loc[datos['sales_amount'].idxmin(), 'sales_date'].strftime("%d/%m/%Y")
    
    print(f"{'Ventas totales:':<30} {total:>12,.2f}")
    print(f"{'Días registrados:':<30} {dias:>12,}")
    print(f"{'Promedio diario:':<30} {promedio:>12,.2f}")
    print(f"{'Venta más alta:':<30} {maximo:>12,.2f} ({dia_max})")
    print(f"{'Venta más baja:':<30} {minimo:12,.2f} ({dia_min})")

def reporte_ventas_por_mes(datos: pd.DataFrame) -> pd.DataFrame:
    por_mes = (
        datos.groupby(['mes','nombre_mes'])['sales_amount']
        .agg(total='sum',promedio='mean', maximo='max')
        .reset_index().sort_values('mes')
    )

    return por_mes

def generar_grafico(datos:pd.DataFrame, por_mes:pd.DataFrame, ruta_salida:str) -> None:

    #creación del lienzo matplotlib
    fig, ax = plt.subplots(figsize=(16, 6), facecolor=COLOR_FONDO)
    
    # Dibujo de linea y el area sombreada
    ax.plot(datos['sales_date'],datos['sales_amount'], color=COLOR_PRINCIPAL, linewidth=1.1, alpha=0.9)
    ax.fill_between(datos['sales_date'], datos['sales_amount'], alpha=0.12, color=COLOR_PRINCIPAL)



    # exportación de imagen
    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=150, bbox_inches="tight")
    plt.close()
    print(f'\n Gráfico exportando en: {ruta_salida}')

#
if __name__=="__main__":
    print(f'Análisis de ventas {RUTA_CSV}')
    try:
        datos = leer_csv(RUTA_CSV)
        reporte_ventas_totales(datos)
        por_mes=reporte_ventas_por_mes(datos)
        generar_grafico(datos,por_mes,RUTA_GRAF)

    except FileNotFoundError as e:
        print(f'ERROR {e}')
    except Exception as e:
        print(f'Error inesperado {e} {type(e)}')