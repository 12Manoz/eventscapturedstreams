#!/bin/bash
# First will create bucket which will be used for deployment
aws s3 mb s3://deployment-dbstreams-test

# this is for packaging using cloudformation

aws cloudformation package --template-file template.yml --s3-bucket deployment-dbstreams-test --s3-prefix myproject/ --output-template-file packaged.yml

# Deployments for cloudformation stack
aws cloudformation deploy --template-file /Users/manopath/Documents/workspace/aws_sample_dbstreams/eventscapturedstreams/packaged.yml --stack-name eventcapturestreams --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM


# this command worked
aws cloudformation package --template-file template.yml --s3-bucket deployment-dbstreams-test

## Delete Stack
aws cloudformation delete-stack --stack-name dynamostreams

## details
stream=arn:aws:dynamodb:us-east-1:554995069609:table/tbff2002_prod_autm_rvis/stream/2022-04-19T16:31:42.091


## deployment of dynamodb 
aws cloudformation package --template-file dbtemplate.yml --s3-bucket deployment-dbstreams-test --s3-prefix dbpacakage/ --output-template-file dbpackaged.yml
aws cloudformation deploy --template-file /Users/manopath/Documents/workspace/aws_sample_dbstreams/eventscapturedstreams/dbpackaged.yml --stack-name notificationcenter --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM


