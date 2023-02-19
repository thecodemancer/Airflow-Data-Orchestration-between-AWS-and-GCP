from datetime import datetime, timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.transfers.s3_to_gcs import S3ToGCSOperator

# Define the default dag arguments
default_args = {
  'owner': 'David',
  'start_date': days_ago(1),
  'depends_on_past': False,
  'email': ['an_email_account@hotmail.com'],
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 2,
  'retry_delay': timedelta(minutes=1)
}

# Dag definition
  my_dag = DAG(
  dag_id='s3_to_gcs',
  default_args=default_args,
  schedule_interval=timedelta(minutes=1440))
  s3_to_gcs_op = S3ToGCSOperator(
  task_id="s3_to_gcs",
  bucket="thecodemancer",
  prefix="Revelo/",
  aws_conn_id='aws_conn_id',
  gcp_conn_id="conn_id",
  dest_gcs="gs://thecodemancer/",
  replace=False,
  gzip=True,
  dag=my_dag,
)

# Set dependencies
s3_to_gcs_op
