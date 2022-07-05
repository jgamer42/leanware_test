
# Leanware technical test

![python-flask](https://img.shields.io/static/v1?label=python&message=flask&color=yellow)
![python-pytest](https://img.shields.io/static/v1?label=python&message=pytest&color=green)
![aws](https://img.shields.io/static/v1?label=AWS&message=DynamoDB&color=red)

## [Documentation](/doc)

## [Project deployed](http://3.226.105.204:5000/)

<h1>Pre-requisites</h1>

- Had installed and runing python3
- Install and configure AWS CLI
- Had IAM user
For this part check [this documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration)

<h1>Test coverage</h1>
<table class="index" data-sortable>
        <thead>
            <tr class="tablehead" title="Click to sort">
                <th class="name left" aria-sort="none" data-shortcut="n">Module</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="s">statements</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="m">missing</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="x">excluded</th>
                <th class="right" aria-sort="none" data-shortcut="c">coverage</th>
            </tr>
        </thead>
        <tbody>
            <tr class="file">
                <td class="name left">src/helpers/auth.py</td>
                <td>20</td>
                <td>5</td>
                <td>0</td>
                <td class="right" data-ratio="15 20">75%</td>
            </tr>
            <tr class="file">
                <td class="name left">src/helpers/date.py</td>
                <td>16</td>
                <td>1</td>
                <td>0</td>
                <td class="right" data-ratio="15 16">94%</td>
            </tr>
            <tr class="file">
                <td class="name left">src/investments.py</td>
                <td>40</td>
                <td>8</td>
                <td>0</td>
                <td class="right" data-ratio="32 40">80%</td>
            </tr>
            <tr class="file">
                <td class="name left">src/managers/__init__.py</td>
                <td>2</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="2 2">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">src/managers/investments.py</td>
                <td>30</td>
                <td>7</td>
                <td>0</td>
                <td class="right" data-ratio="23 30">77%</td>
            </tr>
            <tr class="file">
                <td class="name left">src/managers/traders.py</td>
                <td>21</td>
                <td>2</td>
                <td>0</td>
                <td class="right" data-ratio="19 21">90%</td>
            </tr>
            <tr class="file">
                <td class="name left">src/traders.py</td>
                <td>31</td>
                <td>7</td>
                <td>0</td>
                <td class="right" data-ratio="24 31">77%</td>
            </tr>
            <tr class="file">
                <td class="name left">test/controllers/test_investments.py</td>
                <td>39</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="39 39">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">test/controllers/test_traders.py</td>
                <td>31</td>
                <td>1</td>
                <td>0</td>
                <td class="right" data-ratio="30 31">97%</td>
            </tr>
            <tr class="file">
                <td class="name left">test/helpers/test_auth.py</td>
                <td>10</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="10 10">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">test/helpers/test_date.py</td>
                <td>14</td>
                <td>1</td>
                <td>0</td>
                <td class="right" data-ratio="13 14">93%</td>
            </tr>
            <tr class="file">
                <td class="name left">test/managers/test_investment_manager.py</td>
                <td>28</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="28 28">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">test/managers/test_traders_manager.py</td>
                <td>31</td>
                <td>2</td>
                <td>0</td>
                <td class="right" data-ratio="29 31">94%</td>
            </tr>
        </tbody>
        <tfoot>
            <tr class="total">
                <td class="name left">Total</td>
                <td>313</td>
                <td>34</td>
                <td>0</td>
                <td class="right" data-ratio="279 313">89%</td>
            </tr>
        </tfoot>
    </table>
<h1>How to use</h1>
1. Login to the API
2. Try any route
<h2>routes</h2>

| Route | Method | Use | Payload |
|---|---|---|---|
| /login | POST | This route is used to  Login into the API |{ "username":"your username", "password":"your password" } |
| /logout | GET | This route is used to to Logout from the API | NA |
| /investments/symbols | GET | This route is used to get all available in the API | NA |
| /investments/stocks/<investment_name>/<start_date>/<end_date> | GET | This route ise used to get all prices from a stock in given timeframe - The investment name param is the name of the stock to chekc IE: Google  - The start date param is the start of the  timeframe to check the price , it should be  with following format dd-mm-yyyy   - The end date param is the end of the  timeframe to check the price, this param is optional if let empty will check the price until today, it should be  with following format dd-mm-yyyy | NA |
| /insvestments/sotcks/export | GET | This route is used to a .csv file with the all stocks prices  registre in the API | NA |
| /traders/symbols | GET | This route is used to check which follows the user is following | NA |
| /traders/symbols/update | PUT,POST | This route is used to update which symbols follows the user | {      "Symbols" :["list with symbols to follow"] } 

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

<h1>Steps forward</h1>
- Add integrations test in the endpoints
