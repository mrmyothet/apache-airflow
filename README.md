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

```bash
conda create -n python3.10 python=3.10
conda activate python3.10
pip install apache-airflow
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

### Common Types of Operators

- PythonOperator: Runs python functions
- BashOperator: Execute bash commands
- EmailOperator: Send emails
- SimpleHttpOperator: Make HTTP requests


### Install Conda on WSL

```bash 
wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh

bash Anaconda3-2024.10-1-Linux-x86_64.sh
```