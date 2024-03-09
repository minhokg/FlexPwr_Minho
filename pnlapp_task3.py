from flask import Flask, render_template, jsonify, request, redirect, url_for
from computepnl_task2 import compute_pnl
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def main():
    return redirect(url_for('get_pnl', strategy_id='strategy_1'))


@app.route('/v1/pnl/<string:strategy_id>', methods=['GET'])
def get_pnl(strategy_id):
    pnl_value = compute_pnl(strategy_id=strategy_id, database_path='trades.sqlite',
                            table_name='epex_12_20_12_13')
    response_data = {
        'strategy': strategy_id,
        'value': pnl_value,
        'unit': 'euro',
        'capture_time': datetime.utcnow().isoformat()
    }
    return jsonify(response_data)


if __name__ == "__main__":
    app.run(debug=True)
