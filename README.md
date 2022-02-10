# Simple API (Serverless + Lambda + LocalStack)

## 1. Set up local environment

Follow simple instructions to set up local environment.

### Install [LocalStack](https://localstack.cloud/)

```bash
pip install localstack
```

### Install [Serverless framework](https://www.serverless.com/)

```bash
npm install -g serverless
```

#### Install standalone binary for Serverless framework

```bash
curl -o- -L https://slss.io/install | bash
```

### Install Serverless plugin for LocalStack

```bash
serverless plugin install -n serverless-localstack
```

### Install python requirements plugin for LocalStack

```bash
serverless plugin install -n serverless-python-requirements
```

## 2. Local deployment

### Start LocalStack

```bash
localstack start
```

You can verify that LocalStack is running by checking http://localhost:4566
<br>
You should get:

```
{"status": "running"}
```

Also, you can check the running services by checking https://0.0.0.0:4566/health
<br>
You should get:

```
{"features": {"initScripts": "initialized"}, "services": {"acm": "available", "apigateway": "available", "cloudformation": "available", "cloudwatch": "available", "config": "available", "dynamodb": "available", "dynamodbstreams": "available", "ec2": "available", "es": "available", "events": "available", "firehose": "available", "iam": "available", "kinesis": "available", "kms": "available", "lambda": "available", "logs": "available", "opensearch": "available", "redshift": "available", "resource-groups": "available", "resourcegroupstaggingapi": "available", "route53": "available", "route53resolver": "available", "s3": "available", "secretsmanager": "available", "ses": "available", "sns": "available", "sqs": "available", "ssm": "available", "stepfunctions": "available", "sts": "available", "support": "available", "swf": "available"}, "version": "0.14.0"}
```

### Deploy your service locally

```
serverless deploy --stage local
```

After the deployment you are going to get message from Serverless:

```
Service deployed to stack localstack-test-local
```

And also get information about endpoint and functions that you can use in the service.

```
endpoint: http://localhost:4566/restapis/{YOUR ID}/local/_user_request_

functions:
  get: localstack-tutorial-local-get
  post: localstack-tutorial-local-post
```

## 3. Local usage


* `GET | /hello-world` - get `Hello World` message.

```bash
$ curl -X GET "http://localhost:4566/restapis/{YOUR ID}/local/_user_request_/hello-world"

{
  "result": "Hello World"
}
```

* `POST | /add` - get sum of `Hello World` message.

```bash
curl -X POST "http://localhost:4566/restapis/{YOUR ID}/local/_user_request_/add" \
       -H 'Content-type: application/json' \
       -d '{
           "first": 1,
           "second": 2
       }'

{
  "result": 3
}
```
