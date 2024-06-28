from flask import Blueprint, jsonify
from app.models.employee import get_employee_data

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/api/employees', methods=['GET'])
def employees():
    data = get_employee_data()
    return jsonify(data)
