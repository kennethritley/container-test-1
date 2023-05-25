from flask import Flask, request
import sys

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive():
    message = request.data.decode()
    sys.stderr.write(f'Received message: {message}\n')
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
