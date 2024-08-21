from application.database import db
class Basics(db.Model):
    __tablename__="Basic"
    Index=db.Column(db.Integer,primary_key=True)
    State=db.Column(db.String)
    District=db.Column(db.String)
    Variety=db.Column(db.String)
    Arrival_Date=db.Column(db.String)
    Min_x0020_Price=db.Column(db.Integer)
    Max_x0020_Price=db.Column(db.Integer)
    Modal_x0020_Price=db.Column(db.Integer)
    
    
