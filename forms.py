from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, RadioField, BooleanField, TextAreaField, FileField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, Length

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators = [InputRequired(message="Name is required")])
    species = SelectField('species', choices = [('cat', 'Cat'),('dog', 'Dog'),('porcupine', 'Porcupine')])

    # photo_url = StringField("Photo Link", validators = [Optional()])
    photo_url = StringField("Photo Link", validators = [Optional(), URL()])

    age = IntegerField('Age', validators = [NumberRange(min=0, max=30), Optional()])
    notes = TextAreaField('Notes', validators=[Optional(), Length(min=5)])
    file = FileField('file')
    # available = BooleanField('Available?')

class EditPetForm(FlaskForm):
    # photo_url = StringField("Photo Link", validators = [Optional()])
    photo_url = StringField("Photo Link", validators = [Optional(), URL()])

    notes = TextAreaField('Notes', validators=[Optional(), Length(min=5)])
    available = BooleanField('Available?')