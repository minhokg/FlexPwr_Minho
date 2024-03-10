
from flask import Flask
from task2_computepnl import compute_pnl  # Import the function in task 2
from flask_restx import Api, Resource, reqparse, fields
from datetime import datetime

app = Flask(__name__)
api = Api(app, title="Energy Trading API",
          prefix='/v1',  # Set base_url as v1
          default="Get PnL data", default_label="")
# Define the response data schema with examples
pnl_model = api.model('schema', {
    'strategy': fields.String(example='strategy_1'),
    'value': fields.Float(example=-50),
    'unit': fields.String(example='euro'),
    'capture_time': fields.String(example='2024-03-10T14:33:58.408345')
})

# Build PnL get API


@api.route('/pnl/<string:strategy_id>')  # Set the endpoint as a strategy_id
class PNL(Resource):
    # Put the description on a parameter(strategy_id)
    @api.doc(params={'strategy_id': 'string identifier of a strategy.'})
    # Description on response data and its schema
    @api.response(200, 'A PnL data object.', pnl_model)
    def get(self, strategy_id):
        """
        Returns the pnl of the corresponding strategy.
        """
        pnl_value = compute_pnl(strategy_id=strategy_id, database_path='trades.sqlite',  # Compute the pnl using the second task function
                                table_name='epex_12_20_12_13')
        response = {'strategy_id': strategy_id,
                    'value': pnl_value,
                    'unit': 'euro',
                    'capture_time': datetime.utcnow().isoformat()}
        return response


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
