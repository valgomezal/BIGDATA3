import boto3
import json
from boto3.dynamodb.conditions import Key, Attr


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Animals')

fe = Key('indice').begins_with("C")
pe = "#idx, route, info"
ean = { "#idx": "indice", }
esk = None


response = table.scan(
    FilterExpression=fe,
    ProjectionExpression=pe,
    ExpressionAttributeNames=ean
    )
print(response)
for i in response['Items']:
    print(json.dumps(i))

while 'LastEvaluatedKey' in response:
    response = table.scan(
        ProjectionExpression=pe,
        FilterExpression=fe,
        ExpressionAttributeNames= ean,
        ExclusiveStartKey=response['LastEvaluatedKey']
        )

    for i in response['Items']:
        print(json.dumps(i))