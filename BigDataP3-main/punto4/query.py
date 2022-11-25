import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Animals')

print("Checkeando peces")

response = table.query(
    KeyConditionExpression=Key('indice').eq("Fish")
)

for i in response['Items']:
    print(i)