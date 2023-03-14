from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/sum', methods= ['GET'])
def sum():
    params = request.args.get('sum')
    sum = 0
    for i in params.split(','):
        sum+=int(i)
    return jsonify({'sum': sum, 'service': 'sumV1'})


