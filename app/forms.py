from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class TareaForm(FlaskForm):
    tarea = StringField("Tareas:", validators=[DataRequired()])  #TODO EN LA DOCUMENTACION WTF # PARA PONER TAREAS