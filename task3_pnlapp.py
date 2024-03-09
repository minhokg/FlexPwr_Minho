from flask import Flask, render_template, jsonify, request, redirect, url_for
from task2_computepnl import compute_pnl  # Import the function in task 2
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def main():
    # Show the JSON file of startegy_1 as an example for the initial page
    return redirect(url_for('get_pnl', strategy_id='strategy_1'))


# Customize the last url address like 'strategy_1' or 'strategy_2'
@app.route('/v1/pnl/<string:strategy_id>', methods=['GET'])
def get_pnl(strategy_id):
    """
    Return: JSON file about PnL value and its information
    """
    pnl_value = compute_pnl(strategy_id=strategy_id, database_path='trades.sqlite',
                            table_name='epex_12_20_12_13')
    response_data = {
        'strategy': strategy_id,
        'value': pnl_value,
        'unit': 'euro',
        'capture_time': datetime.utcnow().isoformat()  # Use the current time
    }
    return jsonify(response_data)


if __name__ == "__main__":
    app.run(debug=True)
