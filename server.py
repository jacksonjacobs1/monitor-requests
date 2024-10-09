#%%
from flask import Flask, request
import logging

if __name__ == '__main__':
    app = Flask(__name__)
    werkzeug_logger = logging.getLogger('werkzeug')
    werkzeug_logger.setLevel(logging.ERROR)

    logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s:%(message)s')

    @app.route('/', methods=['POST'])
    def write_to_log():
        log_data = request.json.get('status')
        logging.info(log_data)

        return {'status': 'Message logged successfully'}, 200

    app.run(port=5030)

