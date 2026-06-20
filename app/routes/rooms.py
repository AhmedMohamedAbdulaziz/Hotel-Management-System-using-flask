from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models.room import Room

rooms_bp = Blueprint("rooms", __name__)

@rooms_bp.route("/", methods=["GET"])
def get_all():
    return jsonify([r.to_dict() for r in Room.query.all()]), 200

@rooms_bp.route("/available", methods=["GET"])
def get_available():
    rooms = Room.query.filter_by(Status="Available").all()
    return jsonify([r.to_dict() for r in rooms]), 200

@rooms_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    return jsonify(Room.query.get_or_404(id).to_dict()), 200

@rooms_bp.route("/", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()
    room = Room(
        RoomNumber = data["RoomNumber"],
        Floor      = data.get("Floor"),
        Status     = data.get("Status", "Available"),
        IsSmoking  = data.get("IsSmoking", False),
        RoomTypeID = data["RoomTypeID"],
    )
    db.session.add(room)
    db.session.commit()
    return jsonify(room.to_dict()), 201

@rooms_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update(id):
    room = Room.query.get_or_404(id)
    data = request.get_json()
    for field in ["RoomNumber","Floor","Status","IsSmoking","RoomTypeID"]:
        if field in data:
            setattr(room, field, data[field])
    db.session.commit()
    return jsonify(room.to_dict()), 200

@rooms_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    room = Room.query.get_or_404(id)
    db.session.delete(room)
    db.session.commit()
    return jsonify({"message": "Deleted"}), 200