import json
import boto3
import urllib.parse
 
s3=boto3.client('s3')
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("ReadcontentsfromS3")
 
def lambda_handler(event, context):
    
    bucket= event['Records'][0]['s3']['bucket']['name'] 
    
    
    key= urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
   
    response=s3.get_object(Bucket=bucket, Key=key)
    
    content=response['Body']
    jsonObject=json.loads(content.read())
    Transaction=jsonObject['Transaction']
    
    for record in Transaction:
        table.put_item(
            Item = {
                    "TransactionID" : record['transid'],
                    "TransactionType" : record['transtype'],
                    "Transaction AMount": record['amount']
            }
        )
