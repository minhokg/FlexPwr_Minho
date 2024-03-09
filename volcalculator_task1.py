import sqlite3


class FlexPwrVolCalculator:
    def __init__(self, database_path: str, table_name: str):
        self.database_path = database_path
        self.table_name = table_name

    def compute_total_buy_volume(self, *args, **kwargs) -> float:
        """
        Compute the total buy volume
        Returns: The total buy volume (float)
        """

        try:
            # Connect to the database
            dtbase = sqlite3.connect(self.database_path)
            cursor = dtbase.cursor()

            # Execute SQL query to compute total buy volume
            cursor.execute(
                f"SELECT SUM(QUANTITY) FROM {self.table_name} WHERE SIDE ='buy' ")

            # Retrieve the result
            total_buy_volume = cursor.fetchone()[0]

            # Close the cursor and connection
            cursor.close()
            dtbase.close()

            return total_buy_volume if total_buy_volume is not None else 0
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")

    def compute_total_sell_volume(self, *args, **kwargs) -> float:
        """
        Compute the total sell volume
        Returns: The total sell volume (float)
        """

        try:
            # Connect to the database
            dtbase = sqlite3.connect(self.database_path)
            cursor = dtbase.cursor()

            # Execute SQL query to compute total sell volume
            cursor.execute(
                f"SELECT SUM(quantity) FROM {self.table_name} WHERE SIDE = 'sell' ")

            # Retrieve the result
            total_sell_volume = cursor.fetchone()[0]

            # Close the cursor and connection
            cursor.close()
            dtbase.close()

            return total_sell_volume if total_sell_volume is not None else 0.0

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")


# Try the class with epex_12_20_12_13 table in trades database

try:
    vol_calculator = FlexPwrVolCalculator(
        database_path='trades.sqlite', table_name='epex_12_20_12_13')
    total_buy_volume = vol_calculator.compute_total_buy_volume()
    total_sell_volume = vol_calculator.compute_total_sell_volume()
    print(f"Total buy volume: {total_buy_volume}")
    print(f"Total sell volume: {total_sell_volume}")
except ValueError as e:
    print(f"There is a error: {e}")
