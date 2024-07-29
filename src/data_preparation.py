# %%
# Importar y configurar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de visualización para gráficos
sns.set(style="whitegrid")
pd.set_option('display.max_columns', None)

# Verificar las versiones de las librerías
print(f"Matplotlib version: {plt.matplotlib.__version__}")
print(f"Pandas version: {pd.__version__}")
print(f"Numpy version: {np.__version__}")

# Crear un gráfico simple para verificar Matplotlib
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# %%
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
    if 'Unnamed: 0' in df.columns:
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

# Guardar en un archivo Excel para revisión
output_path = os.path.abspath(os.path.join(current_dir, '../../data/clean/MJ-JUNIO-2024_clean.xlsx'))
df.to_excel(output_path, index=False)
print(f"Datos guardados en {output_path}")


# %%
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de visualización para gráficos
sns.set(style="whitegrid")

# Mostrar todas las columnas de los dataframes
pd.set_option('display.max_columns', None)

# Verificar las versiones de las librerías
print(f"Pandas version: {pd.__version__}")
print(f"Numpy version: {np.__version__}")
print(f"Matplotlib version: {plt.matplotlib.__version__}")

# Ver los primeros registros del DataFrame
print("Primeros registros del DataFrame limpio:\n", df.head())

# Verificar los tipos de datos de cada columna
print("\nTipos de datos del DataFrame:\n", df.dtypes)

# Verificar la existencia de valores nulos
print("\nValores nulos en cada columna:\n", df.isnull().sum())

# Análisis descriptivo básico
print("\nEstadísticas descriptivas del DataFrame:\n", df.describe())

# Histograma de la columna 'Sueldo_Bruto'
plt.figure(figsize=(10, 6))
sns.histplot(df['Sueldo_Bruto'], kde=True, bins=30)
plt.title('Distribución del Sueldo Bruto')
plt.xlabel('Sueldo Bruto')
plt.ylabel('Frecuencia')
plt.show()

# Boxplot de 'Sueldo_Bruto' por 'Sexo'
plt.figure(figsize=(10, 6))
sns.boxplot(x='Sexo', y='Sueldo_Bruto', data=df)
plt.title('Sueldo Bruto por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Sueldo Bruto')
plt.show()


# %%
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Convertir todos los valores de las columnas categóricas a cadenas
categorical_columns = ['Nombre', 'Cargo', 'Area', 'Estatus', 'Sexo']
for col in categorical_columns:
    df[col] = df[col].astype(str)

# Codificar variables categóricas
label_encoders = {}
for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Normalizar y estandarizar las columnas numéricas
numeric_columns = ['Sueldo_Bruto', 'AFP', 'ISR', 'SFS', 'Otros_Descuentos', 'Total_Descuentos', 'Neto']
scaler = StandardScaler()

# Aplicar el escalador solo a las columnas numéricas
df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

# Mostrar las primeras filas del DataFrame después de la codificación y normalización
print("Primeras filas del DataFrame después de la codificación y normalización:\n", df.head())


# %%
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


# %%
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Ruta del archivo Excel limpio
ruta_excel_clean = 'c:\\Users\\bourd\\source\\repos\\IncomeInference\\data\\clean\\MJ-JUNIO-2024_clean.xlsx'
df_clean = pd.read_excel(ruta_excel_clean)

# Convertir la columna 'Fecha_Entrada' a tipo datetime
df_clean['Fecha_Entrada'] = pd.to_datetime(df_clean['Fecha_Entrada'], errors='coerce')

# Crear nueva característica: tiempo en el trabajo en años
df_clean['Tiempo_Trabajo_Anios'] = (pd.Timestamp('now') - df_clean['Fecha_Entrada']).dt.days / 365.25

# Seleccionar las columnas de interés
columns_of_interest = ['Sexo', 'Estatus', 'Area', 'Cargo', 'Tiempo_Trabajo_Anios', 'Total_Descuentos']

# Aplicar LabelEncoder a las columnas categóricas
label_encoders = {}
categorical_columns = ['Sexo', 'Estatus', 'Area', 'Cargo']

for col in categorical_columns:
    le = LabelEncoder()
    df_clean[col] = le.fit_transform(df_clean[col])
    label_encoders[col] = le

# Filtrar y seleccionar las columnas de interés
df_features = df_clean[columns_of_interest]

# Normalizar las características numéricas
numeric_cols = ['Tiempo_Trabajo_Anios', 'Total_Descuentos']
scaler = StandardScaler()
df_features[numeric_cols] = scaler.fit_transform(df_features[numeric_cols])

# Guardar las características seleccionadas en un nuevo archivo Excel
output_features_path = 'c:\\Users\\bourd\\source\\repos\\IncomeInference\\data\\clean\\MJ-JUNIO-2024_features.xlsx'
df_features.to_excel(output_features_path, index=False)
print(f"Características seleccionadas guardadas en {output_features_path}")

# Guardar la etiqueta de salida (Sueldo_Bruto) en otro archivo Excel
output_label_path = 'c:\\Users\\bourd\\source\\repos\\IncomeInference\\data\\clean\\MJ-JUNIO-2024_label.xlsx'
df_clean[['Sueldo_Bruto']].to_excel(output_label_path, index=False, header=True)
print(f"Etiqueta de salida guardada en {output_label_path}")



