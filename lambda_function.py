import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Log the entire event
    logger.info("Received event: " + json.dumps(event, indent=2))
    
    # Process each record in the event
    for record in event['Records']:
        # Extract information about the S3 object
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        
        # Log the details
        logger.info(f"New object created in bucket: {bucket_name}")
        logger.info(f"Object key: {object_key}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('S3 event processed successfully!')
    }
