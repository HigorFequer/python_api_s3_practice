import os
import requests
import json
import boto3
from botocore.exceptions import NoCredentialsError

# Configurações do AWS S3
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
BUCKET_NAME = 'potter-db'
S3_FILE_NAME = 'potterdb_characters.json'
LOCAL_FILE = 'potterdb_characters.json'

def obter_personagens():
    url = 'https://api.potterdb.com/v1/characters'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def salvar_json(dados, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def enviar_para_s3(arquivo_local, bucket, arquivo_s3):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                      aws_secret_access_key=AWS_SECRET_KEY)
    try:
        s3.upload_file(arquivo_local, bucket, arquivo_s3)
        print(f'Arquivo enviado para S3: s3://{bucket}/{arquivo_s3}')
    except NoCredentialsError:
        print('Credenciais AWS não encontradas.')

def ler_do_s3_e_printar(bucket, arquivo_s3):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                      aws_secret_access_key=AWS_SECRET_KEY)
    obj = s3.get_object(Bucket=bucket, Key=arquivo_s3)
    conteudo = obj['Body'].read().decode('utf-8')
    print(conteudo)

if __name__ == '__main__':
    # 1. Obter dados da API
    personagens = obter_personagens()
    # 2. Salvar em JSON
    salvar_json(personagens, LOCAL_FILE)
    # 3. Enviar para o S3
    enviar_para_s3(LOCAL_FILE, BUCKET_NAME, S3_FILE_NAME)
    # 4. Ler do S3 e printar
    ler_do_s3_e_printar(BUCKET_NAME, S3_FILE_NAME)
