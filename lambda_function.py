import json
import boto3
import uuid
from datetime import datetime
from urllib.parse import unquote_plus

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
sns_client = boto3.client('sns')

SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:462532071952:imageuploadalert'
TABLE_NAME = 'imagemetadata'

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)
    
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = unquote_plus(record['s3']['object']['key'])
        file_size = record['s3']['object']['size']
        
        image_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()
        filename = object_key.split('/')[-1]
        
        table.put_item(
            Item={
                'image_id': image_id,
                'filename': filename,
                'file_size': file_size,
                'timestamp': timestamp,
                'bucket_name': bucket_name,
                'object_key': object_key
            }
        )
        
        message = f"""
New Image Uploaded!

File: {filename}
Size: {file_size} bytes ({round(file_size/1024, 2)} KB)
Bucket: {bucket_name}
Time: {timestamp} UTC
Image ID: {image_id}
        """
        
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=f'Image Upload Alert: {filename}',
            Message=message
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Image processed successfully')
    }
