# Try to combine task 1 and 2
# And eliminate the existing duplicate part (database connect and query execute)

import sqlite3


class FlexPwrCalculator:
    def __init__(self, database_path: str, table_name: str):
        self.database_path = database_path
        self.table_name = table_name

    def connect_execute_query(self, sql_query: str, *args, **kwargs) -> float:
        """
        Connect to the database and execute the SQL query
        Args:
        - sql_query (str): The SQL query to execute
        Returns: The result of the query (float)
        """
        try:
            dtbase = sqlite3.connect(self.database_path)
            cursor = dtbase.cursor()
            cursor.execute(sql_query, args)
            result = cursor.fetchone()[0]
            cursor.close()
            return result if result is not None else 0.0
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            return 0.0

    def compute_total_buy_volume(self, *args, **kwargs) -> float:
        """
        Compute the total buy volume
        Returns: The total buy volume (float)
        """
        sql_query = f"SELECT SUM(QUANTITY) FROM {self.table_name} WHERE SIDE ='buy' "
        return self.connect_execute_query(sql_query)

    def compute_total_sell_volume(self, *args, **kwargs) -> float:
        """
        Compute the total sell volume
        Returns: The total sell volume (float)
        """
        sql_query = f"SELECT SUM(quantity) FROM {self.table_name} WHERE SIDE = 'sell' "
        return self.connect_execute_query(sql_query)

    def compute_pnl(self, strategy_id: str, *args, **kwargs) -> float:
        """
        Compute the Profit and Loss (PnL) of each strategy in euros
        Returns: The computed PnL for the specified strategy
        """

        sql_query = f"SELECT SUM(CASE WHEN SIDE='sell' THEN QUANTITY * PRICE ELSE -QUANTITY * PRICE END) " \
                    f"FROM {self.table_name} WHERE strategy = ?"
        return self.connect_execute_query(sql_query, strategy_id)


# Try the class with epex_12_20_12_13 table in trades database

try:
    calculator = FlexPwrCalculator(
        database_path='trades.sqlite', table_name='epex_12_20_12_13')
    # Test tatal buy and sell volume
    total_buy_volume = calculator.compute_total_buy_volume()
    total_sell_volume = calculator.compute_total_sell_volume()
    # Test strategy_1 PnL
    strategy_id = 'strategy_1'
    pnl_strategy1 = calculator.compute_pnl(strategy_id=strategy_id)

    print(f"Total buy volume: {total_buy_volume}")
    print(f"Total sell volume: {total_sell_volume}")
    print(f"The PnL of {strategy_id} is: {pnl_strategy1}")


except ValueError as e:
    print(f"There is a error: {e}")
