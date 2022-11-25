#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

from create_item import create_item

def detect_labels(photo, bucket):

    client=boto3.client('rekognition',region_name='us-east-1')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
        MaxLabels=10)


    print('Detected labels for ' + photo) 
    print()   
    print(response)
    item = create_item(response['Labels'],photo)
    return item
def save_to_database(item):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Animals')
    response = table.put_item(
    Item=item
    )
    return response

def handler(event,context):
    bucketName= event['Records'][0]['s3']['bucket']['name']
    fileName=event['Records'][0]['s3']['object']['key']
    item=detect_labels(fileName, bucketName)
    response = save_to_database(item)
    return response