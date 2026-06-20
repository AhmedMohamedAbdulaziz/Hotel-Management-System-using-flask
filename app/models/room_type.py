from app import db

class RoomType(db.Model):
    __tablename__ = "roomtypes"

    RoomTypeID       = db.Column(db.Integer, primary_key=True)
    TypeName         = db.Column(db.String(100), nullable=False)
    BasePricePerNight= db.Column(db.Numeric(10, 2))
    Capacity         = db.Column(db.Integer)
    Description      = db.Column(db.Text)
    Amenities        = db.Column(db.Text)

    rooms = db.relationship("Room", backref="room_type", lazy=True)

    def to_dict(self):
        return {
            "RoomTypeID":        self.RoomTypeID,
            "TypeName":          self.TypeName,
            "BasePricePerNight": float(self.BasePricePerNight) if self.BasePricePerNight else None,
            "Capacity":          self.Capacity,
            "Description":       self.Description,
            "Amenities":         self.Amenities,
        }