import json
import boto3
import pg8000.dbapi
from botocore.exceptions import ClientError

def get_secret(secret_name, region_name):
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name)
    
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        if 'SecretString' in get_secret_value_response:
            secret = json.loads(get_secret_value_response['SecretString'])
        
        return secret
        
    except ClientError as e:
        raise e

def get_connection_values(connection_name):
    #connnection_name must have the next structure: 'jdbc:redshift://###############.redshift.amazonaws.com:PORT/DB_NAME
    client = boto3.client('glue')
    my_connection_params = {}
    try:
        glue_connection = client.get_connection(Name=connection_name)
        properties = glue_connection['Connection']['ConnectionProperties']
        if properties:
            jbdc_url = properties['JDBC_CONNECTION_URL'].replace('//','').split(':')
            my_connection_params['host'] = jbdc_url[2]
            my_connection_params['database'] = jbdc_url[-1].split('/')[1]
            my_connection_params['port'] = jbdc_url[-1].split('/')[0]
            my_connection_params['username'] = properties['USERNAME']
            my_connection_params['password'] = properties['PASSWORD']

        return my_connection_params
    except Exception as e:
        raise e



def connect_to_redshift(secret_dict = None, glue_connection = None, secret_name = None, region_name = None):

    if secret_dict is None and glue_connection is None and secret_name is None or\
    (secret_name and region_name is None):
        print( """You must pass one of the following parameters:
                1. A dictionary defined by you with the following key/values
                secret_dict = {
                    'username': '',
                    'password': '',
                    'database:' '',
                    'port': '',
                    'host': ''}
                2. Or a name of the glue_connection with the same value/keys as #1
                3. Or a name of the secret with the same value/keys as #1 and region where is located""")
        return 1
                
            
    #Testing without Secrets Manager
    if secret_dict:
        secret_values = secret_dict
    #Using Glue Connections
    elif glue_connection:
        secret_values = glue_connection
    #Using Secrets Manager
    else:
        secret_values = get_secret(secret_name, region_name)   
    
    REDSHIFT_USER = secret_values['username']
    REDSHIFT_PASSWORD = secret_values['password']
    REDSHIFT_DATABASE = secret_values['database']
    REDSHIFT_PORT = secret_values['port']
    REDSHIFT_ENDPOINT = secret_values['host']

    try:
        connection = pg8000.dbapi.connect(
                        database=REDSHIFT_DATABASE,
                        user=REDSHIFT_USER,
                        password=REDSHIFT_PASSWORD,
                        port=REDSHIFT_PORT,
                        host=REDSHIFT_ENDPOINT
        )
        
        return connection
        
    except Exception as e:
        return json.dumps(e, default=str)
        
def write_to_redshift(connection, s3_bucket, prefix, rft_table, role_arn):
    sql= """COPY %s 
           FROM 's3://%s/%s' 
           IAM_ROLE '%s'
           FORMAT AS PARQUET;
           COMMIT;
           """ % (rft_table, s3_bucket, prefix, role_arn)
    
    sql = sql.replace('%3D', '=')

    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        cursor.close()
        connection.close()
        
        return {
            'statusCode': 200,
            'body': json.dumps('Successful write to redshift', default=str)
        }
        
    except Exception as e:
        return json.dumps(e, default=str)