# ETL on Big Data Using PySpark on Google Dataproc

## Problem
**How can we process a huge amount of data
automatically without writing a script repeatedly?**

In this project, you will se how to transform huge size of data from your local storage and store them into
BigQuery as your Data Warehouse. You will see how to process big data using a well-known PySpark package
in one of a Google Cloud Platform service, Dataproc. Running multiple gcloud commands using a bash
script to utilize Google Cloud Platform then resulting a BigQuery table as a data warehouse.
<div align="center">
<img src="https://drive.google.com/uc?export=view&id=1kJ0R11IlHeqLNiPzwD7bwsVkdMUDmLrB">
<small>ETL flow</small>
</div><br />

## Tech Stacks
### PySpark
PySpark is an interface for Apache Spark in Python which allows you to write 
Spark application in Python API. Common methods of pandas for data transformation are doable
in PySpark. PySpark is commonly used to handle big data.
<div align="center">
<img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F2175703%2F06b53d6394cf217240b62d39d3ba6f53%2FPandas%20vs%20Pyspark%201.jpg?generation=1593027654376265&alt=media">
<small>PySpark vs Pandas syntax comparison. Source: https://www.kaggle.com/getting-started/161411</small>
</div><br />

### Dataproc
How do we run PySpark script in Google Cloud? By using Dataproc. Dataproc is a fully managed 
and highly scalable service for running Apache Spark, Apache Flink, Presto, and 30+ open 
source tools and frameworks. Get started with Dataproc by going to this [page](https://cloud.google.com/dataproc).

## Dataset
<div align="center">
<img src="https://drive.google.com/uc?export=view&id=1ONpDeFjjrwAUQ1b_WRHvrIC3XmI-SBrQ">
<small>Flight Data</small>
</div><br />

## Installation
Clone this repository to your preferred directory.
```
git clone https://github.com/eka-pramudita/academi-week3-spark-job
```

## Requirements
- Python 3.6 or above. Check using this command.
```
python --version
```

- Google Cloud SDK. Follow the installation instruction [here](https://cloud.google.com/sdk/docs/install)
then add `.\Google\Cloud SDK\google-cloud-sdk\bin` into your environment variable.
  
- Git. Download from [here](https://git-scm.com/downloads) then install. Add
`C:\Program Files\Git\bin` into your environment variable.
  
## How to Use
1. Open Git Bash terminal.
2. Choose directory using `cd` command to the cloned project directory.
3. I assumed that you already have access to the Google Cloud Platform and set up billing for your project. 
   Configure your Google Cloud by running `gcloud init` command. For step-by-step tutorial please
   refer to [this](https://www.jhanley.com/google-cloud-understanding-gcloud-configurations/#:~:text=A%20gcloud%20configuration%20is%20a,configuration%20named%20default%20is%20created.&text=The%20creation%20of%20a%20configuration%20can%20be%20accomplished%20with%20gcloud%20or%20manually.) page.
   
3. Define variables needed to run the script. Below are the variables you will need to edit.
    ```commandline
    export CLUSTER_NAME=dataproc-pyspark
    export REGION=asia-southeast1
    export BUCKET_NAME=gs://week3
    ```
3. Run the main script using this command. This script wrapped all the data processing steps
   because it contains multiple lines of command. By running this single line of script you
   will not need to run every single line of script in Git Bash.
    ```commandline
    bash bash_script.sh
    ```
   Your cluster will be deleted 5 minutes after job done. Adjust in `max-idle` if you want to change.
6. Check the output in BigQuery.

## Result
<div align="center">
<img src="https://drive.google.com/uc?export=view&id=1uLOZxF3x10F5jSAH9c-CNLNaP07DmTdX">
<small>Transformed Flight Data in Data Warehouse</small>
</div><br />
