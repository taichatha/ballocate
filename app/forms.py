from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired

class LocateForm(Form):
    city_field = StringField(label='City', validators=[DataRequired()])
    state_select_field = SelectField(label='state', validators=[DataRequired()], coerce=int)
    remember_me = BooleanField('remember_me', default=False)