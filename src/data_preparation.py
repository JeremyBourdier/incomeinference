import os
import pandas as pd

# Ruta relativa del archivo Excel
relative_path = '../../data/raw/MJ-JUNIO-2024.xlsx'

# Obtener la ruta absoluta del archivo Excel
current_dir = os.getcwd()
ruta_excel = os.path.abspath(os.path.join(current_dir, relative_path))

# Verificar si el archivo existe
if os.path.exists(ruta_excel):
    print(f"El archivo {ruta_excel} existe en la ruta: {ruta_excel}")
    # Leer el archivo Excel, saltando las primeras filas innecesarias
    df = pd.read_excel(ruta_excel, skiprows=5)
    # Eliminar la columna sin nombre que no contiene datos
    df = df.drop(columns=['Unnamed: 0'])
    # Renombrar columnas
    df.columns = [
        'Numero', 'Nombre', 'Cargo', 'Area', 'Estatus', 'Sexo', 'Fecha_Entrada', 
        'Sueldo_Bruto', 'AFP', 'ISR', 'SFS', 'Otros_Descuentos', 'Total_Descuentos', 
        'Neto'
    ]
    # Mostrar las primeras filas del DataFrame con las columnas renombradas
    print("Primeras filas del DataFrame con columnas renombradas:\n", df.head())
else:
    print(f"El archivo {ruta_excel} no se encontró en la ruta: {ruta_excel}")

# Convertir la columna 'Fecha_Entrada' a tipo datetime
df['Fecha_Entrada'] = pd.to_datetime(df['Fecha_Entrada'], errors='coerce')

# Convertir columnas numéricas a tipo float
cols_to_convert = ['Sueldo_Bruto', 'AFP', 'ISR', 'SFS', 'Otros_Descuentos', 'Total_Descuentos', 'Neto']
df[cols_to_convert] = df[cols_to_convert].apply(pd.to_numeric, errors='coerce')

# Eliminar filas con valores no numéricos
df = df.dropna(subset=cols_to_convert)

# Guardar en un archivo Excel limpio para revisión
output_path = os.path.abspath(os.path.join(current_dir, '../../data/clean/MJ-JUNIO-2024_clean.xlsx'))
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_excel(output_path, index=False)
print(f"Datos guardados en {output_path}")
