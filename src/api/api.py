from flask import Blueprint, jsonify, request
from src.model.Task import Task

# créer ma route
api_bp = Blueprint('api', __name__)

# initialisation de la liste
task_list = []

# route pour avoir une tache
@api_bp.route('/task',methods=['GET'])
def get_tasks():
    return jsonify([task.to_dict() for task in task_list])

@api_bp.route('/task',methods=['POST'])
def create_task():
    data = request.get_json()
    new_task : Task = Task(id=data.get('id'),
                           title=data.get('title'),
                           description=data.get('description'))
    task_list.append(new_task)
    return jsonify(new_task.to_dict()),201

@api_bp.route('/task/<int:task_id>',methods=['DELETE'])
def delete_task(task_id):
    # 1. rechercher la task dans le tableau
    for task in task_list:
        if task.id == task_id:
            task_list.remove(task)
            return jsonify({'message':'task deleted'}), 200
    return jsonify({'message':'task not found'}), 404

@api_bp.route('/task/<int:task_id>',methods=['PUT'])
def update_task(task_id):
    #1. recuperer la data
    data = request.get_json()
    for task in task_list:
        if task.id == task_id:
            task.title = data.get('title')
            task.description = data.get('description')
            task.completed = data.get('completed')
        return jsonify({'message':'task not found'}), 404
