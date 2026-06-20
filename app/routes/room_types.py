from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models.room_type import RoomType

room_types_bp = Blueprint("room_types", __name__)

@room_types_bp.route("/", methods=["GET"])
def get_all():
    return jsonify([r.to_dict() for r in RoomType.query.all()]), 200

@room_types_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    return jsonify(RoomType.query.get_or_404(id).to_dict()), 200

@room_types_bp.route("/", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()
    rt = RoomType(
        TypeName          = data["TypeName"],
        BasePricePerNight = data.get("BasePricePerNight"),
        Capacity          = data.get("Capacity"),
        Description       = data.get("Description"),
        Amenities         = data.get("Amenities"),
    )
    db.session.add(rt)
    db.session.commit()
    return jsonify(rt.to_dict()), 201

@room_types_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update(id):
    rt = RoomType.query.get_or_404(id)
    data = request.get_json()
    for field in ["TypeName","BasePricePerNight","Capacity","Description","Amenities"]:
        if field in data:
            setattr(rt, field, data[field])
    db.session.commit()
    return jsonify(rt.to_dict()), 200

@room_types_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    rt = RoomType.query.get_or_404(id)
    db.session.delete(rt)
    db.session.commit()
    return jsonify({"message": "Deleted"}), 200