# Notification-aws-to-slack

Notify to your slack channel by Incoming Webhook.

This system is building of AWS SAM.

Notification is established with "slackweb" (Python library).

## Preparation

* Get Incoming Webhook URL.
* Install AWS SAM CLI.
* Add slackweb of python library to Lambda function Layers.

## build

```command
sam build
```

## package

```command
sam package \
    --output-template-file packaged.yaml \
    --s3-bucket gnk327-lambda-bucket
```

## deploy

```command
sam deploy \
    --template-file packaged.yaml \
    --stack-name Notifyaws \
    --capabilities CAPABILITY_IAM \
```
