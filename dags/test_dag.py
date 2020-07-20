
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# let's setup arguments for our dag

my_dag_id = "my_first_dag"

# These are applied to all operators
default_args = {
    'owner': 'YOUR_NAME_HERE',
    'depends_on_past': False,
    'retries': 10,
    'concurrency': 1
}

# dag declaration

dag = DAG(
    dag_id=my_dag_id,
    default_args=default_args,
    start_date=datetime(2020, 7, 20),
    catchup=False
    #,schedule_interval=timedelta(minutes=30)
)


# Here's a task based on Bash Operator!

t1 = BashOperator(
    task_id='hello_airflow',
    bash_command="echo 'Hello Airflow!'",
    dag=dag)

t2 =

# Create task T3 to create ~/my_file.txt
# Tip: in Linux, you do that with the following command:
# touch ~/my_file.txt

t3 =

# Create task T4 to rename the file to airflow.txt
# Tip: in Linux, you do that with the following command:
# mv ~/my_file.txt ~/airflow.txt

t4 =

# Last, define the sequence of tasks

t1 >>


