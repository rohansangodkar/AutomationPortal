from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, MultipleFileField
from wtforms.validators import DataRequired, ValidationError


class StandardCheckerForm(FlaskForm):
    def pr_validate(self,pr):
        if len(pr.data) < 9:
            raise ValidationError("Invalid CMM#/H24#")
        if pr.data[:4] != 'CMM-' and pr.data[:4] != 'H24-':
            raise ValidationError("Invalid CMM#/H24#")
    pr = StringField('Please enter your US#/Case# in the CMM-XXXXX/H24-XXXXXX format:', validators=[DataRequired(), pr_validate])
    path = MultipleFileField('Please select files to upload')
    submit = SubmitField('Submit')

