import pandas as pd
import os

input_dir = '/Users/esau/Downloads/analytics/'
output_file = '/Users/esau/Downloads/analytics.csv'
my_sheet_name = 'Conjunto de datos1'
arr = os.listdir(input_dir)

header = ['Fecha', 'Página de destino', 'Sesiones', 'Usuarios', 'Usuarios nuevos', 'Rebotes', 'Transacciones', 'Ingresos', 'Duración de la sesión']
master_df = pd.DataFrame(columns = header)

for file in arr:
    print(input_dir + file)
    try:
        df = pd.read_excel(input_dir + file, sheet_name=my_sheet_name, engine='openpyxl')
        master_df = master_df.append(df)
        print(len(master_df))
    except Exception as e:
        print(e)

master_df.to_csv(output_file)