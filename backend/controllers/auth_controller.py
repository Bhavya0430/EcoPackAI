from flask import request, jsonify
from flask_jwt_extended import create_access_token
from services.auth_service import register_user, authenticate_user

def register():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"message": "All fields are required"}), 400

    user = register_user(username, email, password)

    if not user:
        return jsonify({"message": "User already exists"}), 409

    return jsonify({"message": "User registered successfully"}), 201


def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = authenticate_user(email, password)

    if not user:
        return jsonify({"message": "Invalid email or password"}), 401

    access_token = create_access_token(identity=str(user.id))


    return jsonify({
        "access_token": access_token,
        "user_id": user.id
    }), 200
