from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models.service import Service

services_bp = Blueprint("services", __name__)

@services_bp.route("/", methods=["GET"])
def get_all():
    return jsonify([s.to_dict() for s in Service.query.all()]), 200

@services_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    return jsonify(Service.query.get_or_404(id).to_dict()), 200

@services_bp.route("/", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()
    s = Service(
        ServiceName = data["ServiceName"],
        Price       = data.get("Price"),
        Category    = data.get("Category"),
    )
    db.session.add(s)
    db.session.commit()
    return jsonify(s.to_dict()), 201

@services_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update(id):
    s = Service.query.get_or_404(id)
    data = request.get_json()
    for field in ["ServiceName","Price","Category"]:
        if field in data:
            setattr(s, field, data[field])
    db.session.commit()
    return jsonify(s.to_dict()), 200

@services_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    s = Service.query.get_or_404(id)
    db.session.delete(s)
    db.session.commit()
    return jsonify({"message": "Deleted"}), 200