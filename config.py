# config.py - TEMPORARY for demonstration only
# WARNING: This is NOT safe for production! We'll fix it with Secrets Manager.


import boto3
import json
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "MyTopSecretInfo"
    region_name = "ap-south-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']
    return json.loads(secret)
    credentials = get_secret()
    AWS_ACCESS_KEY_ID = credentials.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = credentials.get("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = credentials.get("AWS_REGION" , boto3.session.Session().region_name "ap-south-1")
