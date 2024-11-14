from flask import Blueprint, request, jsonify
from app.extentions.extentions import bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended import create_access_token, create_refresh_token
from app.container.InstanceContainer import user_service, user_schema

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/v1/auth/login', methods=['POST'])
def login():
    json_data = request.get_json()
    
    account_name = json_data.get('account_name')
    password = json_data.get('password')

    user = user_service.get_user_by_account_name(account_name=account_name)
    if (not user):
        return jsonify({'error': 'Tài khoản không tồn tại', 'status': 404})
    if (not bcrypt.check_password_hash(pw_hash=user.password, password=password)):
        return jsonify({'error': 'Sai mật khẩu', 'status': 404})
    access_token = create_access_token(identity=user)
    refresh_token = create_refresh_token(identity=user)
    user_json = user_schema.dump(user)
    return jsonify({'success': 'Đăng nhập thành công', 'user': user_json, 'access_token': access_token, 'refresh_token': refresh_token, 'status': 200})

@auth_bp.route('/api/v1/auth/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token, status=200)