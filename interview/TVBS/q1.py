from flask import Flask, jsonify, request
from db_users import get_users

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify([])


@app.route('/users')
def get_users_api():

    # Step 1. Get parameters
    name = request.args.get("name")

    # Step 2. Filter out result from db
    users = get_users()
    if name:
        users = [u for u in users if u.get("name") == name]

    return jsonify(users), 200


if __name__ == '__main__':
    app.run()
