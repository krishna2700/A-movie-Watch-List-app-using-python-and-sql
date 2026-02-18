"""
Web Application for Multi-Agent Task Manager
Provides REST API and web interface
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import task_manager as tm
import task_database as db

app = Flask(__name__)
CORS(app)

# Initialize task manager
task_manager = tm.TaskManager()

@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET', 'POST'])
def tasks():
    """Get all tasks or create a new task"""
    if request.method == 'GET':
        main_only = request.args.get('main_only', 'false').lower() == 'true'
        
        if main_only:
            # Return only main tasks
            main_tasks = db.get_main_tasks()
            result = [task_manager.get_task_display_info(task['id']) for task in main_tasks]
        else:
            # Return all tasks with display info
            result = task_manager.list_tasks(show_followups=True)
        
        return jsonify(result)
    
    elif request.method == 'POST':
        data = request.json
        title = data.get('title')
        description = data.get('description', '')
        parent_task_id = data.get('parent_task_id')
        
        if not title:
            return jsonify({'error': 'Title is required'}), 400
        
        if parent_task_id:
            task_id = task_manager.create_followup_task(parent_task_id, title, description)
        else:
            task_id = task_manager.create_main_task(title, description)
        
        task_info = task_manager.get_task_display_info(task_id)
        return jsonify(task_info), 201

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get specific task details"""
    try:
        task_info = task_manager.get_task_display_info(task_id)
        return jsonify(task_info)
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@app.route('/api/tasks/<int:task_id>/start', methods=['POST'])
def start_task(task_id):
    """Start a task with agents"""
    data = request.json
    agent_names = data.get('agent_names', [])
    
    if not agent_names:
        return jsonify({'error': 'At least one agent name is required'}), 400
    
    try:
        status = task_manager.start_task(task_id, agent_names)
        task_info = task_manager.get_task_display_info(task_id)
        return jsonify(task_info)
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@app.route('/api/tasks/<int:task_id>/pause', methods=['POST'])
def pause_task(task_id):
    """Pause agents on a task"""
    data = request.json
    agent_ids = data.get('agent_ids')  # None means pause all
    
    try:
        task_manager.pause_agents(task_id, agent_ids)
        task_info = task_manager.get_task_display_info(task_id)
        return jsonify(task_info)
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@app.route('/api/tasks/<int:task_id>/resume', methods=['POST'])
def resume_task(task_id):
    """Resume paused agents on a task"""
    data = request.json
    agent_ids = data.get('agent_ids', [])
    
    if not agent_ids:
        return jsonify({'error': 'Agent IDs are required'}), 400
    
    try:
        task_manager.resume_agents(task_id, agent_ids)
        task_info = task_manager.get_task_display_info(task_id)
        return jsonify(task_info)
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@app.route('/api/tasks/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    """Mark a task as completed"""
    try:
        task_manager.complete_task(task_id)
        task_info = task_manager.get_task_display_info(task_id)
        return jsonify(task_info)
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@app.route('/api/agents', methods=['GET'])
def get_agents():
    """Get all agents"""
    agents = db.get_all_agents()
    return jsonify(agents)

@app.route('/api/tasks/<int:task_id>/agents', methods=['GET'])
def get_task_agents(task_id):
    """Get agents for a specific task"""
    try:
        agents = db.get_task_agents(task_id)
        return jsonify(agents)
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

if __name__ == '__main__':
    print("Starting Multi-Agent Task Manager Web Application...")
    print("Visit http://localhost:5000 to access the interface")
    app.run(debug=True, host='0.0.0.0', port=5000)
