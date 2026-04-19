import boto3
import os
from datetime import datetime
from config.settings import BUCKET_NAME

def upload_to_s3(file_path):
    s3 = boto3.client('s3')

    base_name = os.path.basename(file_path)
    
    months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
              'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    current_month = months[datetime.now().month - 1]
    
    new_key = f"{current_month}_{base_name}"

    s3.upload_file(
        file_path,
        BUCKET_NAME,
        new_key
    )