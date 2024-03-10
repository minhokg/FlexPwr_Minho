import sqlite3


def compute_pnl(strategy_id: str, database_path: str, table_name: str, *args, **kwargs) -> float:
    """
    Compute the profit and loss (PnL) of each strategy in euros

    Args:
    - strategy_id (str): The ID of the strategy for which to compute PnL.
    - database_path (str): The path to the SQLite database file.
    - table_name (str): The name of the table containing the trade data.

    Returns: The computed PnL for the specified strategy 

    """
    try:
        dtbase = sqlite3.connect(database_path)
        cursor = dtbase.cursor()

        cursor.execute(f"SELECT SUM(CASE WHEN SIDE='sell' THEN QUANTITY * PRICE ELSE -QUANTITY * PRICE END)"
                       f"FROM {table_name} WHERE strategy = ?", (strategy_id,))
        pnl = cursor.fetchone()[0]
        cursor.close()
        dtbase.close()

        return pnl if pnl is not None else 0

    except sqlite3.Error as e:
        print(f"SQLite error : {e}")


# Try the function on strategy_1
try:
    strategy_id = 'strategy_1'
    pnl_value = compute_pnl(
        strategy_id=strategy_id, database_path='trades.sqlite', table_name='epex_12_20_12_13')
    print(f"The PnL of {strategy_id} is: {pnl_value}")
except ValueError as e:
    print(f"There is a error: {e}")
