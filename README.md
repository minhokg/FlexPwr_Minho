# FlexPwr_Minho

* [Background](#Background)
* [Solution](#Solution)
  * [Task1](#Task1)
  * [Task2](#Task2)
  * [Task3](#Task3)

## Background
This repo consists of three solutions for three questions in [**FlexPower QuantChallenge**](https://github.com/FlexPwr/QuantChallenge). Below are simple descriptions of each task. The period spent on solving those problems is from 18:00 pm 08/03/2024 to 9:00 am 11/03/2024 (CET).  
* Task 1: Write two functions for compute buy and sell total volume each.
* Task 2: Write a function computing Profit and Loss for each strategy (PnL)
* Task 3: Expose the function written in task 2 as an entrypoint of a web application

Here, I mostly used Python packages [sqlite3](https://docs.python.org/3/library/sqlite3.html) (task 1 & 2), [flask_restx](https://flask-restx.readthedocs.io/en/latest/) (task 3). Therefore, installing these packages is a prerequisite. Clone the **requirements.txt** and `pip install -r requirements.txt`

## Solution

### Task1 
[task1_volcalculator.py](task1_volcalculator.py)
* Both functions (compute_total_buy_volume, compute_total_sell_volume) have the same arguments: `database_path(str)` and `table_path(str)`. In this task, the database_path is `trades.sqlite` and the table_name is `epex_12_20_12_13`.   
* Combine those two functions as a `class`. Even though it is now overused for only two functions, there is a possibility for adding more functions that require the same arguments later. 
* Calculate the volume in the two functions by using SQL query. For example, in the function `compute_total_buy_function`, the query is like the below
```python
cursor.execute(f"SELECT SUM(QUANTITY) FROM {self.table_name} WHERE SIDE ='buy' ")
```

### Task2 
[task2_computepnl.py](task2_computepnl.py)
* Compared to the task 1, one argument is added: `strategy_id(str)` 
* SQL Query for computing the PnL is the below 
```python
cursor.execute(f"SELECT SUM(CASE WHEN SIDE='sell' THEN QUANTITY * PRICE ELSE -QUANTITY * PRICE END)"
               f"FROM {table_name} WHERE strategy = ?", (strategy_id,))
```

### Task3 
[task3_pnlapi.py](task3_pnlapi.py)

* Run the file by `flask --app task3_pnlapp.py run`. 
* Import the function of task 2
```python
from task2_computepnl import compute_pnl
```
* Define the API first. Set the basepath as a v1
```python
app = Flask(__name__)
api = Api(app, title="Energy Trading API",
          prefix='/v1',  # Set base_url as v1
          default="Get PnL data", default_label="")
```
* Define the scheme of response data. The schema is given in task 3 question. And also include the example
```python
pnl_model = api.model('schema', {
    'strategy': fields.String(example='strategy_1'),
    'value': fields.Float(example=-50),
    'unit': fields.String(example='euro'),
    'capture_time': fields.String(example='2024-03-10T14:33:58.408345')
})
```
* Build the get API. Refer to the annotation of each code. 

```python
@api.route('/pnl/<string:strategy_id>')  # Set the endpoint as a strategy_id
class PNL(Resource):
    # Put the description on a parameter(strategy_id)
    @api.doc(params={'strategy_id': 'string identifier of a strategy.'})
    # Description on response data and its schema
    @api.response(200, 'A PnL data object.', pnl_model)
    def get(self, strategy_id):
        """
        Returns the pnl of the corresponding strategy.
        """
        # Compute the pnl using the second task function
        pnl_value = compute_pnl(strategy_id=strategy_id, database_path='trades.sqlite',
                                table_name='epex_12_20_12_13')
        response = {'strategy_id': strategy_id,
                    'value': pnl_value,
                    'unit': 'euro',
                    'capture_time': datetime.utcnow().isoformat()}
        return response
```

* The API information of the result is quite similar with the task 3 question

```YAML
---
swagger: '2.0'
basePath: "/v1"
paths:
  "/pnl/{strategy_id}":
    get:
      responses:
        '200':
          description: A PnL data object.
          schema:
            "$ref": "#/definitions/schema"
      summary: Returns the pnl of the corresponding strategy
      operationId: get_pnl
      parameters:
      - name: strategy_id
        in: path
        required: true
        type: string
        description: string identifier of a strategy.
      tags:
      - Get PnL data
info:
  title: Energy Trading API
  version: '1.0'
produces:
- application/json
consumes:
- application/json
tags:
- name: Get PnL data
definitions:
  schema:
    properties:
      strategy:
        type: string
        example: strategy_1
      value:
        type: number
        example: -50
      unit:
        type: string
        example: euro
      capture_time:
        type: string
        example: '2024-03-10T14:33:58.408345'
    type: object
responses:
  ParseError:
    description: When a mask can't be parsed
  MaskError:
    description: When any error occurs on mask


```

* Below is the video for simulating the API. 

https://github.com/minhokg/FlexPwr_Minho/assets/90128043/a071bf57-83a2-439c-8eeb-c6a73bad2868




