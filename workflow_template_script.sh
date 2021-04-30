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

#create workflow template
export TEMPLATE_ID=template-demo-1
gcloud dataproc workflow-templates create $TEMPLATE_ID --region $REGION

#create dataproc cluster on workflow template
gcloud dataproc workflow-templates set-managed-cluster $TEMPLATE_ID \
--region=${REGION} \
--cluster-name ${CLUSTER_NAME} \
--master-machine-type n1-standard-2 \
--master-boot-disk-size 20 \
--num-workers 2 \
--worker-machine-type n1-standard-2 \
--worker-boot-disk-size 20 \
--image-version 1.3 \
--max-idle=t5m

#add job
export STEP_ID=add_job
  
gcloud dataproc workflow-templates add-job pyspark pyspark_job.py \
--step-id $STEP_ID \
--workflow-template $TEMPLATE_ID \
--region $REGION \
--jars=gs://spark-lib/bigquery/spark-bigquery-latest.jar

#describe workflow template job
gcloud dataproc workflow-templates describe $TEMPLATE_ID --region $REGION

#instantiate workflow template
gcloud beta dataproc workflow-templates instantiate $TEMPLATE_ID --region $REGION

#delete cluster
gcloud dataproc clusters delete ${CLUSTER_NAME} --region=${REGION}