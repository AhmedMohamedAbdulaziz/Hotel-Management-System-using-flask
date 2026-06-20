from app import db

class ReservationRoom(db.Model):
    __tablename__ = "reservationrooms"

    ReservationRoomId = db.Column(db.Integer, primary_key=True)
    PricePaidPerNight = db.Column(db.Numeric(10, 2))
    ReservationID     = db.Column(db.Integer, db.ForeignKey("reservations.ReservationID"))
    RoomID            = db.Column(db.Integer, db.ForeignKey("rooms.RoomID"))

    def to_dict(self):
        return {
            "ReservationRoomId": self.ReservationRoomId,
            "PricePaidPerNight": float(self.PricePaidPerNight) if self.PricePaidPerNight else None,
            "ReservationID":     self.ReservationID,
            "RoomID":            self.RoomID,
        }