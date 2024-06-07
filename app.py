from flask import Flask, request, jsonify
import os
app = Flask(__name__)
datafile = 'data/data.txt'  
if not os.path.exists(datafile):
    with open(datafile, 'w') as f:
        f.write('')

@app.route('/data', methods=['GET', 'POST'])
def data():
    try:
        if request.method == 'POST':
            new_data = request.json.get('data')
            if new_data:
                with open(datafile, 'a') as f:
                    f.write(f"{new_data}\n")
                return jsonify({"message": "Data saved"}), 201
            return jsonify({"error": "No data provided"}), 400

        if request.method == 'GET':
            with open(datafile, 'r') as f:
                data = f.readlines()
            return jsonify({"data": [line.strip() for line in data]}), 200
    except Exception as e:
        app.logger.error(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

