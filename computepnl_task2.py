import sqlite3


def compute_pnl(database_path: str, table_name: str, strategy_id: str) -> float:
    """
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


try:
    pnl_1 = compute_pnl(database_path="trades.sqlite",
                        table_name="epex_12_20_12_13", strategy_id="strategy_1")
    print(f"PnL of Starategy 1 is {pnl_1} euros")
except Exception as e:
    print(f"An error occurred: {e}")
