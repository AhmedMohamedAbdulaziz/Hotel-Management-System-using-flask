from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models.employee import Employee
from datetime import date, datetime

employees_bp = Blueprint("employees", __name__)

@employees_bp.route("/", methods=["GET"])
@jwt_required()
def get_all_employees():
    employees = Employee.query.all()
    return jsonify([e.to_dict() for e in employees]), 200

@employees_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_employee(id):
    emp = Employee.query.get_or_404(id)
    return jsonify(emp.to_dict()), 200

@employees_bp.route("/", methods=["POST"])
@jwt_required()
def create_employee():
    data = request.get_json()
    hire = data.get("HireDate")
    if hire:
        hire = datetime.strptime(hire, "%Y-%m-%d").date()
    emp = Employee(
        FirstName = data["FirstName"],
        LastName  = data["LastName"],
        Position  = data.get("Position"),
        Email     = data["Email"],
        Phone     = data.get("Phone"),
        HireDate  = hire,
        IsActive  = data.get("IsActive", True),
    )
    
    emp.set_password(data["Password"])
    db.session.add(emp)
    db.session.commit()
    return jsonify(emp.to_dict()), 201

@employees_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_employee(id):
    emp = Employee.query.get_or_404(id)
    data = request.get_json()
    for field in ["FirstName","LastName","Position","Email","Phone","IsActive"]:
        if field in data:
            setattr(emp, field, data[field])
    if "Password" in data:
        emp.set_password(data["Password"])
    db.session.commit()
    return jsonify(emp.to_dict()), 200

@employees_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_employee(id):
    emp = Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    return jsonify({"message": "Employee deleted"}), 200