from app import db

class Reservation(db.Model):
    __tablename__ = "reservations"

    ReservationID       = db.Column(db.Integer, primary_key=True)
    ReservationDate     = db.Column(db.Date)
    CheckInDate         = db.Column(db.Date, nullable=False)
    CheckOutDate        = db.Column(db.Date, nullable=False)
    NumberOfAdults      = db.Column(db.Integer, default=1)
    NumberOfChildren    = db.Column(db.Integer, default=0)
    TotalAmount         = db.Column(db.Numeric(10, 2))
    ReservationStatus   = db.Column(db.String(50), default="Pending")
    SpecialRequests     = db.Column(db.Text)
    CustomerID          = db.Column(db.Integer, db.ForeignKey("customers.CustomerID"))
    CreatedByEmployeeID = db.Column(db.Integer, db.ForeignKey("employees.EmployeeID"))

    rooms    = db.relationship("ReservationRoom",    backref="reservation", lazy=True)
    services = db.relationship("ReservationService", backref="reservation", lazy=True)

    def to_dict(self):
        return {
            "ReservationID":       self.ReservationID,
            "ReservationDate":     str(self.ReservationDate) if self.ReservationDate else None,
            "CheckInDate":         str(self.CheckInDate),
            "CheckOutDate":        str(self.CheckOutDate),
            "NumberOfAdults":      self.NumberOfAdults,
            "NumberOfChildren":    self.NumberOfChildren,
            "TotalAmount":         float(self.TotalAmount) if self.TotalAmount else None,
            "ReservationStatus":   self.ReservationStatus,
            "SpecialRequests":     self.SpecialRequests,
            "CustomerID":          self.CustomerID,
            "CreatedByEmployeeID": self.CreatedByEmployeeID,
        }