from flask import Flask, jsonify, request

app = Flask(__name__)

def fetchBearerToken(auth_token):
    bearer_tokens = {
        'user1': 'phdah',
        'user2': 'dahph',
    }

    auth_token_split = auth_token.split()
    if len(auth_token_split) == 2 and auth_token_split[0].lower() == 'bearer':
        print('Hello')
        if auth_token_split[1] not in bearer_tokens.values():
            return 'invalid'
        else:
            return
    return 'format'

@app.route('/app', methods=['POST'])
def main():
    if 'Authorization' in request.headers:
        token = request.headers['Authorization']
        auth_blocked = fetchBearerToken(token)
        if auth_blocked == 'invalid':
            return jsonify({'message': 'Invalid token', 'code': 401}), 401
        if auth_blocked == 'format':
            return jsonify({'message': 'Incorrect authentication input', 'code': 422}), 422

        name = request.args.get('name', None)

        body_json = request.get_json()
        database = body_json.get('database', None)
        schema = body_json.get('schema', None)
        table = body_json.get('table', None)
        columns = body_json.get('columns', '*')
        respons = {
            'user': name,
            'database': database,
            'schema': schema,
            'table': table,
            'columns': columns,
        }
        return jsonify(respons)
    return jsonify({'message': 'No authentication provided, restricted resource'}), 401

if __name__ == '__main__':
    app.run(debug=True)
