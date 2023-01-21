from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/returnjson', methods=['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
                "Title": "Hello, World",
                "Message": "This is a simple flask json response example",
                }
        return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8123)
