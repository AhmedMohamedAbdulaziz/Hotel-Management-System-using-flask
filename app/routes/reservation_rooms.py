from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models.reservation_room import ReservationRoom

reservation_rooms_bp = Blueprint("reservation_rooms", __name__)

@reservation_rooms_bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    return jsonify([r.to_dict() for r in ReservationRoom.query.all()]), 200

@reservation_rooms_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_one(id):
    return jsonify(ReservationRoom.query.get_or_404(id).to_dict()), 200

@reservation_rooms_bp.route("/", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()
    rr = ReservationRoom(
        PricePaidPerNight = data.get("PricePaidPerNight"),
        ReservationID     = data["ReservationID"],
        RoomID            = data["RoomID"],
    )
    db.session.add(rr)
    db.session.commit()
    db.session.refresh(rr)
    return jsonify(rr.to_dict()), 201

@reservation_rooms_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update(id):
    rr = ReservationRoom.query.get_or_404(id)
    data = request.get_json()
    if "PricePaidPerNight" in data:
        rr.PricePaidPerNight = data["PricePaidPerNight"]
    if "RoomID" in data:
        rr.RoomID = data["RoomID"]
    if "ReservationID" in data:
        rr.ReservationID = data["ReservationID"]
    db.session.commit()
    return jsonify(rr.to_dict()), 200

@reservation_rooms_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    rr = ReservationRoom.query.get_or_404(id)
    db.session.delete(rr)
    db.session.commit()
    return jsonify({"message": "Reservation room deleted"}), 200