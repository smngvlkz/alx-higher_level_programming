from flask import Flask, request, jsonify
import random

app = Flask(__name__)

random_data = [
    {"id": 8446, "name": "amnirqhtfjq"},
    {"id": 7094, "name": "bmofakakhke"},
]

@app.route('/')
def index():
    return "Index"

@app.route('/status_401')
def status_401():
    return "Unauthorized", 401

@app.route('/doesnt_exist')
def doesnt_exist():
    return "Not Found", 404

@app.route('/status_500')
def status_500():
    return "Internal Server Error", 500

@app.route('/post_email', methods=['POST'])
def post_email():
    email = request.form['email']
    return f"Your email is: {email}" 

@app.route('/search_user', methods=['POST'])
def search_user():
    q = request.form.get('q', "")
    if q:
        random_result = random.choice(random_data)
        return jsonify(random_result)
    else:
        return jsonify({})
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
