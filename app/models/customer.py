from app import db


class Customer(db.Model):
    __tablename__ = "customers"

    CustomerID       = db.Column(db.Integer, primary_key=True)
    Fname            = db.Column(db.String(100), nullable=False)
    Lname            = db.Column(db.String(100), nullable=False)
    Email            = db.Column(db.String(150), unique=True, nullable=False)
    Phone            = db.Column(db.String(20))
    Address          = db.Column(db.String(255))
    DateOfBirth      = db.Column(db.Date)
    LoyaltyPoints    = db.Column(db.Integer, default=0)
    RegistrationDate = db.Column(db.Date)

    reservations = db.relationship("Reservation", backref="customer", lazy=True)

    def to_dict(self):
        return {
            "CustomerID":       self.CustomerID,
            "Fname":            self.Fname,
            "Lname":            self.Lname,
            "Email":            self.Email,
            "Phone":            self.Phone,
            "Address":          self.Address,
            "DateOfBirth":      str(self.DateOfBirth) if self.DateOfBirth else None,
            "LoyaltyPoints":    self.LoyaltyPoints,
            "RegistrationDate": str(self.RegistrationDate) if self.RegistrationDate else None,
        }