from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class ProjetForm(FlaskForm):
    titre = StringField('Titre', validators=[DataRequired(), Length(min=3, max=120)])
    slug = StringField('Slug', validators=[DataRequired(), Length(min=3, max=80)])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = StringField('Image', default='images/site01.png')
    tech = StringField('Technologies (Séparées par des virgules)')
    submit = SubmitField('Ajouter Projet') 