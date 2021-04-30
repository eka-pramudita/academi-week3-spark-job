#!/bin/bash

export CLUSTER_NAME=dataproc-pyspark
export REGION=asia-southeast1
export BUCKET_NAME=gs://week3

# transform data according to instruction
python json_edit.py

# upload data to Google Cloud Storage
gsutil cp output/2021-04-*.csv $BUCKET_NAME

#enable gcloud services
gcloud services enable compute.googleapis.com \
  dataproc.googleapis.com \
  bigquerystorage.googleapis.com

#create dataset
gcloud alpha bq datasets create flight_data

#create dataproc cluster
gcloud beta dataproc clusters create ${CLUSTER_NAME} \
--region=${REGION} \
--master-machine-type n1-standard-2 \
--master-boot-disk-size 20 \
--num-workers 2 \
--worker-machine-type n1-standard-2 \
--worker-boot-disk-size 20 \
--image-version 1.3 \
--max-idle=t5m

#submit jobs
gcloud dataproc jobs submit pyspark pyspark_job.py \
--cluster=${CLUSTER_NAME} \
--region=${REGION} \
--driver-log-levels root=FATAL \
--jars=gs://spark-lib/bigquery/spark-bigquery-latest.jar

#delete cluster
gcloud dataproc clusters delete ${CLUSTER_NAME} --region=${REGION}