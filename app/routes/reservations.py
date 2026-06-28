from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models.reservation import Reservation
from datetime import date , datetime

reservations_bp = Blueprint("reservations", __name__)

@reservations_bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    return jsonify([r.to_dict() for r in Reservation.query.all()]), 200

@reservations_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_one(id):
    return jsonify(Reservation.query.get_or_404(id).to_dict()), 200

@reservations_bp.route("/", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()
    checkin  = datetime.strptime(data["CheckInDate"],  "%Y-%m-%d").date()
    checkout = datetime.strptime(data["CheckOutDate"], "%Y-%m-%d").date()
    res = Reservation(
        ReservationDate     = date.today(),
        CheckInDate         = checkin,
        CheckOutDate        = checkout,
        NumberOfAdults      = data.get("NumberOfAdults", 1),
        NumberOfChildren    = data.get("NumberOfChildren", 0),
        TotalAmount         = data.get("TotalAmount"),
        ReservationStatus   = data.get("ReservationStatus", "Pending"),
        SpecialRequests     = data.get("SpecialRequests"),
        CustomerID          = data["CustomerID"],
        CreatedByEmployeeID = data["CreatedByEmployeeID"],
    )

    checkin  = datetime.strptime(data["CheckInDate"],  "%Y-%m-%d").date()
    checkout = datetime.strptime(data["CheckOutDate"], "%Y-%m-%d").date()
    db.session.add(res)
    db.session.commit()
    return jsonify(res.to_dict()), 201

@reservations_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update(id):
    res = Reservation.query.get_or_404(id)
    data = request.get_json()
    if "CheckInDate" in data:
        res.CheckInDate = datetime.strptime(data["CheckInDate"], "%Y-%m-%d").date()
    if "CheckOutDate" in data:
        res.CheckOutDate = datetime.strptime(data["CheckOutDate"], "%Y-%m-%d").date()
    for field in ["NumberOfAdults", "NumberOfChildren", "TotalAmount",
                  "ReservationStatus", "SpecialRequests"]:
        if field in data:
            setattr(res, field, data[field])
    db.session.commit()
    return jsonify(res.to_dict()), 200

@reservations_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    res = Reservation.query.get_or_404(id)
    db.session.delete(res)
    db.session.commit()
    return jsonify({"message": "Deleted"}), 200