# OpenSearch SIGv4 IAM Auth
OpenSearch supports multiple authentication types. The simplest is basic authentication, IAM authentication can also be used. To use IAM authentication requests need to be signed with a Sigv4 authentication header.

The following repository demonstrates how map and IAM user to an OpenSearch role, then how to use the IAM user to make requests to the OpenSearch domain.

Follow the instructions below to walk through an example

1. Run the CloudFormation stack below

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=open-sigv4&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/opensearchpy_Sigv4.yaml)

The resources created by the CloudFormation stack are documented in the architecture below

2. Navigate to the to the [opensearch-user on the IAM console](https://us-east-1.console.aws.amazon.com/iam/home#/users/opensearch-user?section=security_credentials) and create an access key

3. Log into OpenSearch dashboard, map the ARN of the IAM user to an OpenSearch role

3. Run python script
