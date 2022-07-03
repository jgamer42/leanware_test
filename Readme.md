
# Leanware technical test 
![python-flask](https://img.shields.io/static/v1?label=python&message=flask&color=yellow)
![python-pytest](https://img.shields.io/static/v1?label=python&message=pytest&color=green)
![aws](https://img.shields.io/static/v1?label=AWS&message=DynamoDB&color=red)

## [Documentation](/doc)
<h1> Pre-requisites</h1>

- Had installed and runing python3
- Install and configure AWS CLI
- Had IAM user
For this part check [this documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration)

<h1>Installation</h1>

This tutorial is only fonr unix based systems

1. Create a virtual enviroment

```bash
python3 -m venv env
```

2. Start the virtualenv

```bash
source env/bin/activate
```

3. install the dependencies

```bash
pip install -r requeriments.txt
```

4. Create a reports folder

```bash
mkdir reports
```

5. Create a .env file , and put the content from .env.example
6. Fill the .env file
7. Run the main.py

```bash
python main.py
```
