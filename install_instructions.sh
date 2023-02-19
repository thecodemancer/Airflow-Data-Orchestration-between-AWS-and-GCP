mkdir ./dags ./plugins ./logs
echo -e "AIRFLOW_UID=$(id -u) \nAIRFLOW_GID=0" > .env
docker compose up airflow-init
docker ps
docker compose up
docker ps
docker exec 929393993939 airflow version
curl -X GET "https://localhost:8080/api/v1/dags"
