# Apache Airflow

### Install Apache Airflow

```bash
python -m venv airflow_venv
source airflow_venv/bin/activate

pip install apache-airflow
```

- got error while installing and suggest to install rustup

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

##### For development

```bash
airflow standalone
```

##### For production

```bash
airflow db init
airflow webserver -p 8080
airflow scheduler
```
