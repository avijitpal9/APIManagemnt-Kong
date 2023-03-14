from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/div', methods= ['GET'])
def div():
    params = request.args.get('div')
    dividend= params.split(',')[0]
    divisor= params.split(',')[1]
    quotient = int(dividend)/int(divisor)
    
    return jsonify({'quotient': quotient, 'service': 'divV1'})
