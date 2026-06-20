from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models.customer import Customer
from datetime import date, datetime

customers_bp = Blueprint("customers", __name__)

@customers_bp.route("/", methods=["GET"])
@jwt_required()
def get_all_customers():
    customers = Customer.query.all()
    return jsonify([c.to_dict() for c in customers]), 200

@customers_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return jsonify(customer.to_dict()), 200

@customers_bp.route("/", methods=["POST"])
@jwt_required()
def create_customer():
    data = request.get_json()

    # Convert string dates to Python date objects
    dob = data.get("DateOfBirth")
    if dob:
        dob = datetime.strptime(dob, "%Y-%m-%d").date()

    customer = Customer(
        Fname            = data["Fname"],
        Lname            = data["Lname"],
        Email            = data["Email"],
        Phone            = data.get("Phone"),
        Address          = data.get("Address"),
        DateOfBirth      = dob,
        LoyaltyPoints    = data.get("LoyaltyPoints", 0),
        RegistrationDate = date.today(),
    )
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.to_dict()), 201

@customers_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_customer(id):
    customer = Customer.query.get_or_404(id)
    data = request.get_json()
    for field in ["Fname","Lname","Email","Phone","Address","LoyaltyPoints"]:
        if field in data:
            setattr(customer, field, data[field])
    db.session.commit()
    return jsonify(customer.to_dict()), 200

@customers_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": "Customer deleted"}), 200