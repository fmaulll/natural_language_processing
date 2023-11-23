from flask import Flask, request, jsonify
import nlp
import text_blob

app = Flask(__name__)

# Define an endpoint for handling POST requests
@app.route('/api/post_example', methods=['POST'])
def post_example():
    data = request.json  # Get the JSON data from the request

    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400  # Return an error response

    # Process the received data (you can replace this with your own logic)
    response_data = {"message": "Received data:", "data": text_blob.predicted_category(data['report'])}

    return jsonify(response_data), 200  # Return a JSON response

if __name__ == '__main__':
    app.run(debug=True)