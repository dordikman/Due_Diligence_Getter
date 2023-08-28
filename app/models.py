from app import db


class User(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    first_name =db.Column(db.String,nullable=False)
    last_name =db.Column(db.String,nullable=False)
    email =db.Column(db.String,nullable=False)
    credit_rating =db.Column(db.String,nullable=False)
    credit_number =db.Column(db.Integer,unique=True,nullable=False)




