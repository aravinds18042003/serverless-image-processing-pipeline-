# Serverless Image Processing Pipeline

## Architecture
S3 → Lambda → DynamoDB + SNS

## Services Used
- AWS S3
- AWS Lambda (Python 3.12)
- AWS DynamoDB
- AWS SNS
- AWS IAM

## How It Works
1. Image uploaded to S3 triggers Lambda automatically
2. Lambda extracts metadata (filename, size, timestamp)
3. Metadata stored in DynamoDB with UUID partition key
4. SNS sends email alert within 5 seconds

## Screenshots

### S3 Bucket


![S3](Screenshot_20260607_190445~2.jpg)




![S3](Screenshot_20260607_190456~2.jpg)




![S3](Screenshot_20260607_190501~2.jpg)




![S3](Screenshot_20260607_190542~2.jpg)




![S3](Screenshot_20260607_190645~2.jpg)



### DynamoDB Entry


![DynamoDB](Screenshot_20260607_192556~2.jpg)




![DynamoDB](Screenshot_20260607_192640~2.jpg)




![DynamoDB](Screenshot_20260607_192652~2.jpg)




![DynamoDB](Screenshot_20260607_192802~2.jpg)



### CloudWatch Logs


![CloudWatch](Screenshot_20260607_194631~2.jpg)




![CloudWatch](Screenshot_20260607_194820~2.jpg)




![CloudWatch](Screenshot_20260607_195216~2.jpg)




![CloudWatch](Screenshot_20260607_195232~2.jpg)



### SNS Email Alert


![SNS](Screenshot_20260607_195853~2.jpg)




![SNS](Screenshot_20260607_195901~2.jpg)
