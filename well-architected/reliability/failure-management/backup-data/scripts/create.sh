#!/usr/bin/env bash
# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# or in the "license" file accompanying this file. This file is distributed 
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
# express or implied. See the License for the specific language governing 
# permissions and limitations under the License.



templatebucket=$1
templateprefix=$2
stackname=$3
region=$4
backupbucket=$5
prefix=$6
SCRIPTDIR=`dirname $0`
if [ "$templatebucket" == "" ]
then
    echo "Usage: $0 <template bucket> <template prefix> <stack name> <region> <backup bucket name> <ingress prefix> <--update>"
    exit 1
fi
if [ "$templateprefix" == "" ]
then
    echo "Usage: $0 <template bucket> <template prefix> <stack name> <region> <backup bucket name> <ingress prefix> <--update>"
    exit 1
fi
if [ "$stackname" == "" ]
then
    echo "Usage: $0 <template bucket> <template prefix> <stack name> <region> <backup bucket name> <ingress prefix> <--update>"
    exit 1
fi
if [ "$region" == "" ]
then
    echo "Usage: $0 <template bucket> <template prefix> <stack name> <region> <backup bucket name> <ingress prefix> <--update>"
    exit 1
fi
if [ "$backupbucket" == "" ]
then
    echo "Usage: $0 <template bucket> <template prefix> <stack name> <region> <backup bucket name> <ingress prefix> <--update>"
    exit 1
fi
if [ "$prefix" == "" ]
then
    echo "Usage: $0 <template bucket> <template prefix> <stack name> <region> <backup bucket name> <ingress prefix> <--update>"
    exit 1
fi
UPDATE=${7:-""}    
CFN_CMD="create-stack"
if [ "$UPDATE" == "--update" ]
then
    CFN_CMD="update-stack"
    echo "Updating stack"
fi

# Check if we need to append region to S3 URL
TEMPLATE_URL=https://s3.amazonaws.com/$templatebucket/$templateprefix/workload.yaml
if [ "$region" != "us-east-1" ]
then
    TEMPLATE_URL=https://s3-$region.amazonaws.com/$templatebucket/$templateprefix/workload.yaml
fi

echo "Uploading CFN scripts"
aws s3 sync $SCRIPTDIR/../cfn s3://$templatebucket/$templateprefix

echo "Packaging ec2 producer code"
aws s3 cp $SCRIPTDIR/../src/tweetmaker.py s3://$templatebucket/code/tweetmaker.py
aws s3 cp $SCRIPTDIR/../glue/compaction.py s3://$templatebucket/code/compaction.py

aws cloudformation $CFN_CMD --stack-name $stackname \
    --template-url $TEMPLATE_URL \
    --tags Key=Project,Value=BackupRestoreAnalytics \
    --parameters \
    ParameterKey=AllowedPrefixIngress,ParameterValue=$prefix \
    ParameterKey=Bucket,ParameterValue=$templatebucket \
    ParameterKey=ReplBucketName,ParameterValue=$backupbucket \
    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM

# The deploy script
# ./scripts/create.sh template-bucket-443 cfn BackupRestore us-east-1 mybackupbucket-443 pl-001f6b2921aca88a4 
