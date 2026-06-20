from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models.reservation_service import ReservationService
from datetime import datetime

reservation_services_bp = Blueprint("reservation_services", __name__)

@reservation_services_bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    return jsonify([rs.to_dict() for rs in ReservationService.query.all()]), 200

@reservation_services_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_one(id):
    return jsonify(ReservationService.query.get_or_404(id).to_dict()), 200

@reservation_services_bp.route("/", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()
    rs = ReservationService(
        Quantity      = data.get("Quantity", 1),
        TotalPrice    = data.get("TotalPrice"),
        OrderDateTime = datetime.utcnow(),
        ReservationID = data["ReservationID"],
        ServiceId_FK  = data["ServiceID"],
        EmployeeID    = data["EmployeeID"],
    )
    db.session.add(rs)
    db.session.commit()
    return jsonify(rs.to_dict()), 201

@reservation_services_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    rs = ReservationService.query.get_or_404(id)
    db.session.delete(rs)
    db.session.commit()
    return jsonify({"message": "Deleted"}), 200