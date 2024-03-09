# FlexPwr_Minho

* [Background](#Background)
* [Solution](#Solution)
  * [Task1](#Task1)
  * [Task2](#Task2)
  * [Task3](#Task3)
* [Setup](#Setup)

## Background
This repo consists of three solutions for three tasks in [**FlexPower QuantChallenge**](https://github.com/FlexPwr/QuantChallenge). 

## Solution

### Task1 ([task1_volcalculator.py](task1_volcalculator.py))
* Both functions (compute_total_buy_volume, compute_total_sell_volume) have the same arguments: `database_path(str)` and `table_path(str)`. In this task, the database_path is `trades.sqlite` and the table_name is `epex_12_20_12_13`.   
* I combined those two functions as a **class**. Even though it is now overused for only two functions, there is a possibility for adding more functions that require the same arguments later. 
* I calculated the volume in the two functions by using SQL query. For example, in the function `compute_total_buy_function`, the query is like the below
```python
cursor.execute(f"SELECT SUM(QUANTITY) FROM {self.table_name} WHERE SIDE ='buy' ")
```

### Task2 ([task2_computepnl.py](task2_computepnl.py))
* Compared to the task 1, one argument is added: `strategy_id(str)` 
* But same as task 1, here I also used SQL Query for computing the PnL like below 
```python
cursor.execute(f"SELECT SUM(CASE WHEN SIDE='sell' THEN QUANTITY * PRICE ELSE -QUANTITY * PRICE END)"
               f"FROM {table_name} WHERE strategy = ?", (strategy_id,))
```

### Task3 ([task3_pnlapp.py](task3_pnlapp.py))
Here, I import the function in task 2
```python
from task2_computepnl import compute_pnl
```

The results for the strategy 1 & 2 are the below pictures. 

<div style="display: flex; justify-content: space-between;">
    <img src="pics/strategy_1.png" alt="strategy_1" style="width: 48%;"/>
    <img src="pics/strategy_2.png" alt="strategy_2" style="width: 48%;"/>
</div>


