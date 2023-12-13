from flask import Flask, request, jsonify, render_template

import nlp
import text_blob
import send_email

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def report(name=None):
    return render_template('index.html', name=name)

# Define an endpoint for handling POST requests

@app.route('/api/post_example', methods=['POST'])
def post_example():
    data = request.json  # Get the JSON data from the request

    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400  # Return an error response
    data_authorities = text_blob.predicted_category(data['report'])

    if data_authorities['predicted_authorities']:
        send_email.send_email("reporter@gmail.com", data['report'], data_authorities['predicted_authorities']) 
        response_data = {"message": "Received data:", "data": data_authorities}
    else:
        response_data = {"message": "Invalid Report, please make new report"}
        # Process the received data (you can replace this with your own logic)

    return jsonify(response_data), 200  # Return a JSON response

if __name__ == '__main__':
    app.run(debug=True)