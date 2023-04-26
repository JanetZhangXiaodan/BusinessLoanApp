from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, allow_headers=['Content-Type', 'Content-Length', 'Access-Control-Allow-Origin',
                         'Access-Control-Allow-Headers', 'Access-Control-Allow-Methods'])

@app.route('/getfinaloutcome', methods=['POST'])
def decideLoanAmount():
    content_type = request.headers.get('Content-Type')
    loan_amount = 0
    if request.method == 'POST' and content_type == 'application/json':
        loan_request = request.json
        print('>>>>>>>>>> loan_request', loan_request)
        if loan_request.get('loanAmount') and loan_request.get('preAssessment') and float(loan_request.get('loanAmount'))>0:
            loan_amount = float(loan_request.get('loanAmount'))
            pre_assessment = int(loan_request.get('preAssessment'))

            if pre_assessment == 60:
                loan_amount *= 0.6
            elif pre_assessment == 100:
                return jsonify({'outcome': True, 'loanamount': loan_amount})
            elif pre_assessment == 20: 
                loan_amount *= 0.2
                return jsonify({'outcome': False, 'loanamount': loan_amount})

        return jsonify({'outcome': True, 'loanamount': loan_amount})
    else:
        return jsonify({'error': 'Content-Type not supported!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=True)
