from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from flask_uploads import configure_uploads, IMAGES, UploadSet
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['UPLOADED_IMAGES_DEST'] = 'static'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home():
    """Home page of pets"""
    pets = Pet.query.all()
    return render_template('pet_list.html', pets = pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Add a pet to the list"""
    form = AddPetForm()
    if form.validate_on_submit():
        # name = form.name.data
        # species = form.species.data
        # photo_url = form.photo_url.data
        # age = form.age.data
        # notes = form.notes.data
        # available = form.available.data

        # pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes, available = available)

        data = {k: v for k,v in form.data.items() if k != 'csrf_token' and k != 'file'}
        new_pet = Pet(**data)
        filename = images.save(form.file.data)

        if filename != None:
            new_pet.photo_url = f'static/{filename}'

        db.session.add(new_pet)
        db.session.commit()
        flash(f'{new_pet.name} is added.')
        return redirect('/')
    else:
        return render_template('add_pet.html', form = form)
    
@app.route('/pets/<int:id>')
def pet_detail(id):
    """Get pet's detail"""
    pet = Pet.query.get_or_404(id)
    return render_template('pet_detail.html', pet = pet)

@app.route('/pets/<int:id>/edit', methods=['GET', 'POST'])
def pet_edit(id):
    """Edit a pet"""
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj = pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()
        flash(f'{pet.name} is added.')
        return redirect(f'/pets/{pet.id}')
    else:
        return render_template('pet_edit.html', form = form)


