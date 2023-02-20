# Airflow - Data Orchestration between AWS and GCP
An AirFlow Dag that moves S3 Bucket Files to Google Cloud Storage. Keeping the same folder partitioning and file formats.

## The Mission

Write an AirFlow Dag that moves S3 Bucket Files to Google Cloud Storage. Keeping the same folder partitioning and file formats.

## The Constraints

- Avoid billing
- Keep it simple

## The Approach

For this mission we’re going to deploy Apache Airflow with the Docker Compose method on Google Cloud’s Cloud Shell. We could have used Google Cloud’s Cloud Composer but with this approach we’re avoiding billing.

In this DAG we’re going to copy data from s3://thecodemancer/Revelo/ to gs://thecodemancer/Revelo/. We could have done this by coding from scratch but Airflow has a rich set of Operators ready to import, configure and use. Having said that, we’ll use the S3ToGCSOperator for simplicity.


<img src="https://github.com/thecodemancer/Airflow-Data-Orchestration-between-AWS-and-GCP/blob/f08d8fbdcb6488f736b17dfc9534ef4370c0175f/images/airflow3.png" />

<img src="https://github.com/thecodemancer/Airflow-Data-Orchestration-between-AWS-and-GCP/blob/f08d8fbdcb6488f736b17dfc9534ef4370c0175f/images/airflow8.png" />

<img src="https://github.com/thecodemancer/Airflow-Data-Orchestration-between-AWS-and-GCP/blob/f08d8fbdcb6488f736b17dfc9534ef4370c0175f/images/airflow10.png" />
