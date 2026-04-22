from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='frontend', static_url_path='')

# Endpoint for executing tasks
@app.route('/api/execute_task', methods=['POST'])
def execute_task():
    task = request.json.get('task')
    # Logic to execute the task
    return jsonify({'status': 'Task executed', 'task': task})

# Endpoint for status updates
@app.route('/api/status', methods=['GET'])
def status():
    # Logic to get current status
    return jsonify({'status': 'All systems operational'})

# Endpoint for memory management
@app.route('/api/memory', methods=['GET'])
def memory():
    # Logic to get memory usage
    return jsonify({'memory_usage': '50%'})

# Serve frontend dashboard
@app.route('/', methods=['GET'])
def dashboard():
    try:
        return send_from_directory('frontend', 'index.html')
    except:
        return "<h1>Dashboard</h1><p>Welcome to the Autonomous Agent Dashboard!</p>"

# Fallback for static files
@app.route('/<path:path>')
def serve_static(path):
    try:
        return send_from_directory('frontend', path)
    except:
        return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))