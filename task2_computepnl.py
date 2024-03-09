import sqlite3


def compute_pnl(strategy_id: str, database_path: str, table_name: str) -> float:
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


# Try the function on strategy_1 with epex_12_20_12_13 table in trades database

try:
    pnl_1 = compute_pnl(strategy_id="strategy_1", database_path="trades.sqlite",
                        table_name="epex_12_20_12_13")
    print(f"PnL of Starategy 1 is {pnl_1} euros")
except Exception as e:
    print(f"An error occurred: {e}")
