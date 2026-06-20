from app import db, bcrypt

class Employee(db.Model):
    __tablename__ = "employees"

    EmployeeID = db.Column(db.Integer, primary_key=True)
    FirstName  = db.Column(db.String(100), nullable=False)
    LastName   = db.Column(db.String(100), nullable=False)
    Position   = db.Column(db.String(100))
    Email      = db.Column(db.String(150), unique=True, nullable=False)
    Phone      = db.Column(db.String(20))
    HireDate   = db.Column(db.Date)
    IsActive   = db.Column(db.Boolean, default=True)
    Password   = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.Password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.Password, password)

    def to_dict(self):
        return {
            "EmployeeID": self.EmployeeID,
            "FirstName":  self.FirstName,
            "LastName":   self.LastName,
            "Position":   self.Position,
            "Email":      self.Email,
            "Phone":      self.Phone,
            "HireDate":   str(self.HireDate) if self.HireDate else None,
            "IsActive":   self.IsActive,
        }