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

def connect_to_redshift(database_name, secret_name = None, region_name = None, secret = None):
    '''
    secret = {
        'username': '',
        'password': '',
        'port': '',
        'host': ''
    }
    '''
    if database_name is None:
        return 'the parameter database_name is mandatory'

    if secret is None:
        secret = get_secret(secret_name, region_name)   
    
    REDSHIFT_USER = secret['username']
    REDSHIFT_PASSWORD = secret['password']
    REDSHIFT_DATABASE = database_name
    REDSHIFT_PORT = secret['port']
    REDSHIFT_ENDPOINT = secret['host']

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