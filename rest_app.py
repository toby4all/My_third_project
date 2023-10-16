from flask import Flask, request
from flask import jsonify
from db_connector import add_user, get_user, delete_user, update_user
import os
import signal
app = Flask(__name__)

# supported methods
@app.route('/users/<int:user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        user_name = request_data.get('name')
        if user_id > 2:
            add_user(user_id, user_name)
            return jsonify({'user id': user_id, 'user name': user_name, 'status': 'saved'}, + 200)  # status code
        else:
            return jsonify({'status': 'error', 'reason': 'id already exist'}, + 500)  # status cod
    elif request.method == 'GET':
        if user_id in range(0,6):
            user_name = get_user(user_id)
            return jsonify({'status': 'ok', 'user_name': user_name}, 200 ) # status code
        else:
            return jsonify({'status': 'error', 'reason': 'no such id'}, +500 ) # status code
    elif request.method == 'PUT':
        request_data = request.json
        user_name = request_data.get('name')
        if user_id in range(0, 2):
            update_user(user_id, user_name)
            return jsonify({'status': 'ok', 'user_name': user_name}, + 200)   # status code
        else:
            return jsonify({'status': 'error', 'reason': 'no such id'}, + 500)   # status code
    elif request.method == 'DELETE':
        request_data = request.json
        user_name = request_data.get('user_id')
        if user_id in range(0,2):
            delete_user(user_id)
            return jsonify({'status': 'ok', 'user_deleted': user_name}, + 200 ) # status code
        else:
            return jsonify({'status': 'error', 'reason': 'no such id'}, + 500 ) # status code

@app.route("/stop_server")   # route to stop server
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'



app.run(host='127.0.0.1', debug=True, port=5000)