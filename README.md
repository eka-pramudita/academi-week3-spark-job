# ETL on Big Data Using Dataproc

## Problem
“How can we process a huge amount of data
automatically without writing a script repeatedly?”

This project is about transforming the data and storing them into
BigQuery as your Data Warehouse.

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
2. `cd` to cloned project directory.
3. Configure your Google Cloud by running `gcloud init` command. For step-by-step tutorial please
   refer [this](https://www.jhanley.com/google-cloud-understanding-gcloud-configurations/#:~:text=A%20gcloud%20configuration%20is%20a,configuration%20named%20default%20is%20created.&text=The%20creation%20of%20a%20configuration%20can%20be%20accomplished%20with%20gcloud%20or%20manually.) page.
3. Define variables needed to run the script. Below are the variables you will need to edit.
    ```commandline
    export CLUSTER_NAME=dataproc-pyspark
    export REGION=asia-southeast1
    export BUCKET_NAME=gs://week3
    ```
3. Run the main script using this command.
    ```commandline
    bash bash_script.sh
    ```
   Your cluster will be deleted 5 minutes after job done. Adjust in `max-idle`.
6. Check the output in BigQuery.
7. Run workflow template script using this command.
   ```commandline
   bash workflow_template_script.sh
    ```