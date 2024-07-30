import pandas as pd
import os

# Ruta de los archivos de características de cada nómina
ruta_nomina1 = 'c:\\Users\\bourd\\source\\repos\\IncomeInference\\data\\clean\\MJ-JUNIO-2024_features.xlsx'
ruta_nomina2 = 'c:\\Users\\bourd\\source\\repos\\IncomeInference\\data\\clean\\Prueba MJ-JUNIO-2024_features.xlsx'
ruta_nomina3 = 'c:\\Users\\bourd\\source\\repos\\IncomeInference\\data\\clean\\Prueba2 MJ-JUNIO-2024_features.xlsx'

# Verificar si los archivos existen
def verificar_existencia_archivo(ruta):
    if os.path.exists(ruta):
        print(f"El archivo {ruta} existe.")
        return True
    else:
        print(f"El archivo {ruta} no se encontró.")
        return False

archivo1_existe = verificar_existencia_archivo(ruta_nomina1)
archivo2_existe = verificar_existencia_archivo(ruta_nomina2)
archivo3_existe = verificar_existencia_archivo(ruta_nomina3)

# Cargar los datasets si existen
df_nomina1 = pd.read_excel(ruta_nomina1) if archivo1_existe else pd.DataFrame()
df_nomina2 = pd.read_excel(ruta_nomina2) if archivo2_existe else pd.DataFrame()
df_nomina3 = pd.read_excel(ruta_nomina3) if archivo3_existe else pd.DataFrame()

# Mostrar las primeras filas de cada dataset para verificación
if not df_nomina1.empty:
    print("Primeras filas de Nomina 1:\n", df_nomina1.head())
if not df_nomina2.empty:
    print("Primeras filas de Nomina 2:\n", df_nomina2.head())
if not df_nomina3.empty:
    print("Primeras filas de Nomina 3:\n", df_nomina3.head())

# Unificar los datasets no vacíos
dfs = [df_nomina1, df_nomina2, df_nomina3]
df_unificado = pd.concat([df for df in dfs if not df.empty], ignore_index=True)

# Mostrar las primeras filas del DataFrame unificado
print("Primeras filas del DataFrame unificado:\n", df_unificado.head())

# Ruta para guardar el archivo unificado
ruta_unificado = 'c:\\Users\\bourd\\source\\repos\\IncomeInference\\data\\clean\\nominas_unificadas.xlsx'

# Guardar el archivo unificado
if not df_unificado.empty:
    df_unificado.to_excel(ruta_unificado, index=False)
    print(f"Archivo unificado guardado en: {ruta_unificado}")
else:
    print("No se encontraron archivos para unificar.")
