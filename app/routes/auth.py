from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models.employee import Employee

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email    = data.get("Email")
    password = data.get("Password")

    employee = Employee.query.filter_by(Email=email).first()
    if not employee or not employee.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=str(employee.EmployeeID))
    return jsonify({"token": token, "employee": employee.to_dict()}), 200