from flask import Flask, render_template, jsonify
import database

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/agent/hello', methods=['POST'])
def agent_hello():
    # Multi-agent endpoint
    return jsonify({
        'status': 'success',
        'message': 'hello',
        'agent': 'hello-agent'
    })

if __name__ == '__main__':
    database.create_tables()
    app.run(debug=True, host='0.0.0.0', port=5000)
