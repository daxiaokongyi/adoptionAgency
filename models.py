from flask_sqlalchemy import SQLAlchemy

GENERAL_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

db = SQLAlchemy()

def connect_db(app):
    """Connect this database with the provided flask app"""
    db.app = app    
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = 'pet'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), nullable = False)
    species = db.Column(db.String(50), nullable = False)
    photo_url = db.Column(db.String(150), nullable = True)
    age = db.Column(db.Integer, nullable = True)
    notes = db.Column(db.String(50), nullable = True)
    available = db.Column(db.Boolean, default = True, nullable = False)

    def __repr__(self):
        """Show info about pet"""
        return f"<Pet name = {self.name} age = {self.age}>"

    def image_url(self):
        """Set image link with a default link if no link available"""
        return self.photo_url or GENERAL_IMAGE