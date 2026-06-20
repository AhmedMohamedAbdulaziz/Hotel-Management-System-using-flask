from app import db

class Service(db.Model):
    __tablename__ = "services"

    ServiceID   = db.Column(db.Integer, primary_key=True)
    ServiceName = db.Column(db.String(150), nullable=False)
    Price       = db.Column(db.Numeric(10, 2))
    Category    = db.Column(db.String(100))

    def to_dict(self):
        return {
            "ServiceID":   self.ServiceID,
            "ServiceName": self.ServiceName,
            "Price":       float(self.Price) if self.Price else None,
            "Category":    self.Category,
        }