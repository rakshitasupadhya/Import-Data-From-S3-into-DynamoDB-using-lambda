# Import-Data-From-S3-into-DynamoDB-using-lambda

This is a demonstartion on how S3 Object triggers lambda function and loads the contents to DynamoDB

# Architecture
<img width="412" alt="image" src="https://github.com/rakshitasupadhya/Import-Data-From-S3-into-DynamoDB-using-lambda/assets/107621546/76f315e4-82cb-418e-9d61-0395488a87e9">

# Implementation
1. Create S3 Bucket
   <img width="872" alt="image" src="https://github.com/rakshitasupadhya/Import-Data-From-S3-into-DynamoDB-using-lambda/assets/107621546/aecaca7b-4093-4761-90fd-4ad6c6f1cbc2">
2. create DynamoDB table by specifying Partition key
   <img width="881" alt="image" src="https://github.com/rakshitasupadhya/Import-Data-From-S3-into-DynamoDB-using-lambda/assets/107621546/fe491aa8-085a-4899-b7db-bec53e3f8ac1">
3. Create Lambda function and add Role - S3ReadOnlyAccess & DynamoDBFUllAccess policies to it
   <img width="896" alt="image" src="https://github.com/rakshitasupadhya/Import-Data-From-S3-into-DynamoDB-using-lambda/assets/107621546/24cbc313-a1fa-4888-b5f0-af9468c75733">
   <img width="655" alt="image" src="https://github.com/rakshitasupadhya/Import-Data-From-S3-into-DynamoDB-using-lambda/assets/107621546/7c6c25cb-9e87-47f0-a229-accbd9f62c03">
4. Add trigger event in S3 under Properties tab(Trigger must be updated automatically in Lambda)
   <img width="823" alt="image" src="https://github.com/rakshitasupadhya/Import-Data-From-S3-into-DynamoDB-using-lambda/assets/107621546/f472116f-1ae1-460c-808f-02623763e08d">

6. Upload Transaction file in S3 and check the DynamoDB for the contents
   ![image](https://github.com/rakshitasupadhya/Import-Data-From-S3-into-DynamoDB-using-lambda/assets/107621546/ffa84500-af6a-4205-b974-4ab5d71438a1)
   ![image](https://github.com/rakshitasupadhya/Import-Data-From-S3-into-DynamoDB-using-lambda/assets/107621546/aa41f11f-16f0-495c-9f36-6aad0b31075e)
