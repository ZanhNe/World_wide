from flask import Blueprint, jsonify, request
from app.presentation.models.models import User
from app.container.InstanceContainer import user_service, user_schema
from app.extentions.extentions import bcrypt

user_bp = Blueprint('user', __name__)

@user_bp.route('/api/v1/users', methods=['GET'])
def get_all_users():
    results = user_service.get_all_users()
    return user_schema(results, many=True)

@user_bp.route('/api/v1/users', methods=['POST'])
def add_user():
    json_data = request.get_json()
    user_name = json_data.get('user_name')
    account_name = json_data.get('account_name')
    password = json_data.get('password')
    if (not user_name or not account_name or not password):
        return jsonify({'error': 'Vui lòng nhập đầy đủ thông tin', 'status': 400})
    
    hash_pass = bcrypt.generate_password_hash(password=password)
    user = User(user_name=user_name, account_name=account_name, password=hash_pass)
    user_after_add = user_service.add_user(user=user)
    if (not user_after_add):
        return jsonify({'error': 'Lỗi khi thêm (Trùng account_name,...)', 'status': 400})
    user_json = user_schema.dump(user_after_add)
    return jsonify({'success': 'Thêm thành công', 'status': 200, 'user': user_json})