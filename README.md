# 📊 Análisis de Ventas Comerciales

Proyecto realizado en Python para analizar un conjunto de datos simulados de ventas comerciales y generar indicadores básicos sobre el desempeño de una empresa.

---

# 🎯 Objetivo

Analizar información de ventas para obtener métricas relevantes como:

- Ventas totales
- Ventas por mes
- Evolución de ventas mediante gráficos

---

# 📁 Estructura del Proyecto

```bash
📦 proyecto-ventas
 ┣ 📂 datos
 ┃ ┗ ventas.csv
 ┣ 📂 scripts
 ┃ ┗ analisis_ventas.py
 ┣ 📂 resultados
 ┃ ┗ grafico_ventas.png
 ┣ 📜 README.md
 ┗ 📜 .gitignore
```

---

# 📄 Dataset

El archivo CSV contiene los siguientes campos:

| Campo | Descripción |
|--------|-------------|
| id | Identificador de la venta |
| sale_date | Fecha de la venta |
| sale_amount | Monto de la venta |

## Ejemplo de datos

```csv
id,sale_date,sale_amount
1,2026-01-10,15000
2,2026-01-15,22000
3,2026-02-01,18000
```

---

# ⚙️ Funcionalidades

El proyecto permite:

✅ Importar datos desde un archivo CSV  
✅ Calcular ventas totales  
✅ Analizar ventas por mes  
✅ Generar gráficos de evolución de ventas  

---

# 📈 Indicadores Generados

## Ventas Totales

Suma total de todos los montos registrados en `sale_amount`.

## Ventas Mensuales

Agrupación de ventas por mes utilizando la fecha registrada en `sale_date`.

---

# 📊 Visualización

Se genera un gráfico simple que representa la evolución de ventas mensuales utilizando la librería `Matplotlib`.

---

# 🛠️ Tecnologías Utilizadas

- Python
- Pandas
- Matplotlib

---

# 📂 Resultados

Los gráficos y archivos generados se almacenan en la carpeta:

```bash
resultados/
```

---

# 🚀 Posibles Mejoras

- Agregar más indicadores
- Dashboard interactivo
- Exportación automática de reportes
- Integración con base de datos
- Comparativas entre períodos

---

# 👨‍💻 Autor
- Andres Bonelli
- Héctor Signoriello

Proyecto desarrollado con fines educativos para la practica de gestión colaborativa, control de versiones y organizacion emprezarial.
