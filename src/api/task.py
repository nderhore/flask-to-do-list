from flask import Blueprint, render_template

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def template_task():
    return render_template('tasks/task_list.html')