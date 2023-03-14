from flask import Flask, jsonify, request

app = Flask(__name__)
print("__name__ is {}".format(__name__))
@app.route('/sum', methods= ['GET'])
def sum():
    params = request.args.get('sum')
    sum = 0
    for i in params.split(','):
        sum+=float(i)
    return jsonify({'sum': sum, 'service': 'sumV2'})

