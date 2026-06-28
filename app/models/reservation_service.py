from app import db

class ReservationService(db.Model):
    __tablename__ = "reservationservices"

    ReservationServiceID = db.Column(db.Integer, primary_key=True, autoincrement=True)  # ✅ primary key واضح
    Quantity             = db.Column(db.Integer, default=1)
    TotalPrice           = db.Column(db.Numeric(10, 2))
    OrderDateTime        = db.Column(db.DateTime)
    ReservationID        = db.Column(db.Integer, db.ForeignKey("reservations.ReservationID"))
    ServiceID            = db.Column(db.Integer, db.ForeignKey("services.ServiceID"))
    EmployeeID           = db.Column(db.Integer, db.ForeignKey("employees.EmployeeID"))

    def to_dict(self):
        return {
            "ReservationServiceID": self.ReservationServiceID,
            "Quantity":             self.Quantity,
            "TotalPrice":           float(self.TotalPrice) if self.TotalPrice else None,
            "OrderDateTime":        str(self.OrderDateTime) if self.OrderDateTime else None,
            "ReservationID":        self.ReservationID,
            "ServiceID":            self.ServiceID,
            "EmployeeID":           self.EmployeeID,
        }