from flask_wtf import FlaskForm
from wtforms import DateField, StringField, FloatField, SubmitField  #Tipos de campos de wtforms
from wtforms.validators import DataRequired, Length, ValidationError  #Validador de wtforms para que un campo no este vacio
from datetime import date

class MovementsForm(FlaskForm):  #Esta clase es de Flask-WTF para validacion de formularios. 
    #Las variables no van con self porque son propias de FlaskForm
    date = DateField('Fecha', validators=[DataRequired(message="La fecha es requerida")])  #Con esto podemos reemplazar el campo para completar de html por el objeto.date
    concept = StringField('Concepto', validators=[DataRequired(message="El concepto es requerido"), Length(min=4, message="El concepto debe tener mas de cuatro caracteres")])
    quantity = FloatField('Monto', validators=[DataRequired(message="El monto es requerido")])
    submit = SubmitField('Aceptar')


    def validate_date(form, field):
        if field.data > date.today():
            raise ValidationError("Fecha invalida: la fecha no debe ser mayor a hoy")  #Esta clase salta automaticamente cuando se cumple la condicion. No hay que llamarla en ningun lado