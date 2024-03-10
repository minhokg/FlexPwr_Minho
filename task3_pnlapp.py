from flask import Flask
from flask_restx import Api, Resource, reqparse
from task2_computepnl import compute_pnl  # Import the function in task 2
from datetime import datetime

app = Flask(__name__)
api = Api(app, title="Energy Trading API")

parser = reqparse.RequestParser()
parser.add_argument('strategy_id', type=str, required=True,
                    help='string identifier of a strategy.')  # Modified description


@api.route('/pnl/<strategy_id>')
class PNL(Resource):
    @api.doc(summary="Return")
    def get(self, strategy_id):
        pnl_value = compute_pnl(strategy_id=strategy_id, database_path='trades.sqlite',
                                table_name='epex_12_20_12_13')

        return {
            'strategy': strategy_id,
            'value': pnl_value,
            'unit': 'euro',
            'capture_time': datetime.utcnow().isoformat()  # Use the current time
        }
