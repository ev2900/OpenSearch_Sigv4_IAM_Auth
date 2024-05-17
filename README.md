# OpenSearch SIGv4 IAM Auth

<img width="275" alt="map-user" src="https://img.shields.io/badge/cloudformation template deployments-6-blue"> <img width="85" alt="map-user" src="https://img.shields.io/badge/views-508-green"> <img width="125" alt="map-user" src="https://img.shields.io/badge/unique visits-168-green">

OpenSearch supports multiple authentication types. The simplest is basic authentication, IAM authentication can also be used. To use IAM authentication requests need to be signed with a Sigv4 authentication header.

The following repository demonstrates how map and IAM user to an OpenSearch role, then how to use the IAM user to make requests to the OpenSearch domain.

Follow the instructions below to walk through an example

1. Run the CloudFormation stack below

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=open-sigv4&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/opensearch_Sigv4.yaml)

The resources created by the CloudFormation stack are documented in the architecture below

<img width="250" alt="map-user" src="https://github.com/ev2900/OpenSearch_Sigv4_IAM_Auth/blob/main/README/architecture.png">

2. Navigate to the to the [opensearch-user on the IAM console](https://us-east-1.console.aws.amazon.com/iam/home#/users/opensearch-user?section=security_credentials) and create an access key

3. Create a AWS CLI profile to store the access key Id and secret access key ```aws configure --profile os-profile```

4. Log into OpenSearch dashboard, map the ARN of the IAM user to an OpenSearch role

<img width="500" alt="map-user" src="https://github.com/ev2900/OpenSearch_Sigv4_IAM_Auth/blob/main/README/Map_User.png">

5. Update and run python script. There are two python scripts you can run. Both do the same thing but use different python libraries. The [opensearchpy_Sigv4.py](https://github.com/ev2900/OpenSearch_Sigv4_IAM_Auth/blob/main/opensearchpy_Sigv4.py) script uses the [opensearch-py](https://opensearch-project.github.io/opensearch-py/) python library to make requests. The [requests_Sigv4.py](https://github.com/ev2900/OpenSearch_Sigv4_IAM_Auth/blob/main/requests_Sigv4.py) uses the more generic [requests](https://pypi.org/project/requests/) library to make requests to OpenSearch.

Update the *host* and *region* variables in the [opensearchpy_Sigv4.py](https://github.com/ev2900/OpenSearch_Sigv4_IAM_Auth/blob/main/opensearchpy_Sigv4.py) python script.

Update the *host*, *path* and *region* variables in the [requests_Sigv4.py](https://github.com/ev2900/OpenSearch_Sigv4_IAM_Auth/blob/main/requests_Sigv4.py) python script.

Then save and run the script(s)
