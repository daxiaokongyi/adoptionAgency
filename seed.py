from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Empty table if it is not empty
Pet.query.delete()

# Add sample pet
p1 = Pet(name='Tom', species='Cat', photo_url='https://static.scientificamerican.com/sciam/cache/file/92E141F8-36E4-4331-BB2EE42AC8674DD3_source.jpg', age=1)
p2 = Pet(name='Jack', species='Dog', photo_url='https://www.dogtime.com/assets/uploads/2011/03/puppy-development-1280x720.jpg', age=2)
p3 = Pet(name='Lemon', species='Tutle', photo_url='https://www.wildlifedepartment.com/sites/default/files/Mississippi%20Map%20Turtle_Website.jpg', age=2, available = False)

db.session.add_all([p1,p2,p3])
db.session.commit()