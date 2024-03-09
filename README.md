# FlexPwr_Minho

* [Background](#Background)
* [Solution](#Solution)
  * [Task1] (#Task1)
  * [Task2] (#Task2)
  * [Task3] (#Task3)
* [Setup](#Setup)

## Background
This repo consists of three solutions for three tasks in![**FlexPower QuantChallenge**](https://github.com/FlexPwr/QuantChallenge). 

## Solution
* For task 1 and 2, I use **sqlite3** packages and SQL queries for calculating the value(buy_volume, sell_volume, PnL).
* For task 3, I use **flask** packages for API application, resulting in a JSON file. 
### Task1
Here, the main point is a **class**. I combined two functions (compute_total_buy_volume, compute_total_sell_volume). Even though it is now overused for only two functions, there is a possibility for adding more functions that require the same arguments later. 

### Task2
Here, I import the function in task 2
```{python}
from task2_computepnl import compute_pnl
```

The results for strategy_1 & 2 are the below pictures. 

<div style="display: flex; justify-content: space-between;">
    <img src="pics/strategy_1.png" alt="strategy_1" style="width: 48%;"/>
    <img src="pics/strategy_2.png" alt="strategy_2" style="width: 48%;"/>
</div>


