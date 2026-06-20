from app import db

class Room(db.Model):
    __tablename__ = "rooms"

    RoomID     = db.Column(db.Integer, primary_key=True)
    RoomNumber = db.Column(db.String(20), nullable=False)
    Floor      = db.Column(db.Integer)
    Status     = db.Column(db.String(50), default="Available")
    IsSmoking  = db.Column(db.Boolean, default=False)
    RoomTypeID = db.Column(db.Integer, db.ForeignKey("roomtypes.RoomTypeID"))

    def to_dict(self):
        return {
            "RoomID":     self.RoomID,
            "RoomNumber": self.RoomNumber,
            "Floor":      self.Floor,
            "Status":     self.Status,
            "IsSmoking":  self.IsSmoking,
            "RoomTypeID": self.RoomTypeID,
        }