# Airflow Tutorial

## Preparation Steps

**1. Activate Windows Subsystem for Linux (WSL)**

From a PowerShell prompt with Administrative access:

`dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`

**2. Install Ubuntu 18LTS from the Microsoft Store**

**3. Install Python Dependencies**

We will use Python 3.7, pip and venv for our demo. In case you don't have them:

`sudo apt-get update
sudo apt-get upgrade python3
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo apt-get update
sudo apt install python3-pip
sudo apt install -y python3-venv`

**4. Create a new folder for your project, e.g. airflow-tutorial**

**5. From this folder, create a virtual environment and activate it**

`python3 -m venv venv
source venv/bin/activate`

**6. Install airflow**

`pip install apache-airflow`

**7. Run the initial configuration**

`export AIRFLOW_HOME=$(pwd)
airflow initdb`
