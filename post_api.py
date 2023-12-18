from flask import Flask, request, jsonify, render_template

import nlp
import svm
import send_email

app = Flask(__name__)

@app.route('/')
def report(name=None):
    return render_template('index.html', name=name)

# Define an endpoint for handling POST requests

@app.route('/api/example', methods=['POST'])
def example():
    data = request.json  # Get the JSON data from the request
    response_data = {"message": "Received data:", "data": data}

    print(response_data)
    return jsonify(response_data), 200  # Return a JSON response

@app.route('/api/post_example', methods=['POST'])
def post_example():
    data = request.json['data']  # Get the JSON data from the request
    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400  # Return an error response
    
    data_authorities = svm.predicted_category(data['report'])
    print(data_authorities)

    if data_authorities['predicted_category']:
        send_email.send_email(data['email'], data['report'], data_authorities['predicted_category']) 
        response_data = {"message": "Received data:", "data": {"predicted_category": data_authorities['predicted_category'], "name": send_email.send_to_name(data_authorities['predicted_category'])}}
    else:
        response_data = {"message": "Invalid Report, please make new report"}
        # Process the received data (you can replace this with your own logic)

    return jsonify(response_data), 200  # Return a JSON response

if __name__ == '__main__':
    app.run(debug=True)