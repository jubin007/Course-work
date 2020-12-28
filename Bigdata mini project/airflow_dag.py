#!/usr/bin/python3

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from utils import *
import datetime


default_args = {
    'owner': 'jubin',
    'depends_on_past': False,
    'start_date': datetime.datetime.strptime('2020-12-03', '%Y-%m-%d'),
    'email': ['monitoring@your_domain.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': datetime.timedelta(minutes=200),
}

# Create the DAG
dag = DAG('daily_analytics_etl',
    default_args=default_args,
    schedule_interval='46 10 * * *',
      catchup=False)

# task
task1_execute = """/usr/bin/python3.6 ~/projects/etl/join.py"""
extract_task = BashOperator(
    task_id='execute_etl',
    bash_command=task1_execute,
    dag=dag)
