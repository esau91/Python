import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import logging

def get_auth(secrets_file):
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name(secrets_file, scope)

    try:
        client = gspread.authorize(creds)
        logging.info('Authentication succedd')

    except Exception as e:
        logging.exception('The following error happend when trying to authenticate: ')
        exit(1)

    return client


def get_sheets_file(client, file_name, sheet_name, skip_rows= 0): #, secrets_file):
    
    try:
        spreadsheet = client.open(file_name)
        sheet = spreadsheet.worksheet(sheet_name)
        logging.info("The file '{}' was successfully accessed".format(file_name))

    except Exception as e:
        logging.exception('The following error happend when trying to access the file: ')
        exit(1)
    
    raw_data = pd.DataFrame(sheet.get_all_values()[skip_rows:])
    headers = raw_data.iloc[0]
    raw_df = raw_data[1:]
    raw_df.columns = headers
    df_shape = raw_df.shape
    logging.info('File loaded with {} rows and {} columns.'.format(df_shape[0], df_shape[1]))

    return raw_df


def output_format(input_df, column_names, to_date):
    formatted_df = input_df.loc[:, column_names]

    for column in to_date:
        if column in formatted_df.columns:
            formatted_df[column] = (pd.to_datetime(formatted_df[column])).dt.strftime('%d/%m/%Y')
        else:
            logging.error("The column name '{}' was not found".format(column))

    return formatted_df


def write_to_sheets(client, file_name, sheet_name, input_df):

    spreadsheet = client.open(file_name)
    sheet = spreadsheet.worksheet(sheet_name)
    current_rows_len = len(sheet.get_all_values())
    try:
        set_with_dataframe(sheet, input_df, include_column_header=True, row= current_rows_len + 1)
    except Exception as e:
        logging.exception('The following error happend while trying to write: ')
        exit(1)


def main():

    logging.basicConfig(level=logging.DEBUG)
    secrets_file = '' #path to secrets file
    output_file_name = 'Master Welchs'

    config_values = {
        'Analytics': {
            'file_name': 'Analytics',
            'sheet_name': 'Raw',
            'columns': ['Campaña', 'Contenido del anuncio', 'Fecha ga', 'INGRESOS'],
            'columns_to_date': ['Fecha ga'],
            'skip_rows': 0,
            'output_sheet_name': 'Analytics'
            },
        'Google Ads Plataforma': {
            'file_name': 'Google Ads Plataforma',
            'sheet_name': 'Google Ads Plataforma',
            'columns': ['Campaña','Grupo de anuncios','Día','Moneda','Clics','Impresiones','Costo','Video reproducido al 100%'],
            'columns_to_date': ['Día'],
            'skip_rows': 2,
            'output_sheet_name': 'Google_ads_pfm'
            },
        'Facebook': {
            'file_name': 'Facebook',
            'sheet_name': 'Raw',
            'columns': ['Nombre de la campaña', 'Nombre del conjunto de anuncios', 'Nombre del anuncio', 'Día', 'Divisa', 'Clics en el enlace', 'Impresiones', 'Inversion', 'Reproducciones de video hasta el 100%'],
            'columns_to_date': ['Día'],
            'skip_rows': 0,
            'output_sheet_name': 'Facebook'
            }
    }
    
    input_source = 'Analytics'

    client = get_auth(secrets_file)
    raw_df = get_sheets_file(client, config_values[input_source]['file_name'],  config_values[input_source]['sheet_name'], config_values[input_source]['skip_rows'])
    formatted_df = output_format(raw_df, config_values[input_source]['columns'], config_values[input_source]['columns_to_date'])
    write_to_sheets(client, output_file_name, config_values[input_source]['output_sheet_name'], formatted_df)
    logging.info('Successful execution')

if __name__ == '__main__':
    main()


