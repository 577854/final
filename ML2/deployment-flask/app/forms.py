from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):
    
    #occupation = 
    #race = BooleanField(label='Are you white')
    #countryChoises = ['United-States','Mexico','Philippines','Germany','Canada','Puerto-Rico','El-Salvador','India','Cuba','England','Jamaica','South','China','Japan','Vietnam',
    #            'Dominican-Republic','Guatemala','Italy','Poland','Columbia','Taiwan','Haiti','Iran','Portugal','France','Peru','Nicaragua','Greece','Ecuador','Thailand',
    #            'Ireland','Cambodia','Laos','Trinadad&Tobago','Yugoslavia','Hungary','Hong','Honduras','Outlying-US(Guam-USVI-etc)','Scotland','Holand-Netherlands','other']
    #country = SelectField('Native country', choises=countryChoises)
    country = BooleanField(label='Is your native country USA')

    age = IntegerField('Age. ', validators=[NumberRange(min=17, max=90)])

    workclassChoises = [('Private','Private'),('Self-emp-not-inc','Self-emp-not-inc'),('Local-gov','Local-gov'),
                        ('State-gov','State-gov'),('Self-emp-inc','Self-emp-inc'),('Federal-gov','Federal-gov'),
                        ('Without-pay','Without-pay'),('Never-worked','Never-worked'),('?','other')]
    workclass = SelectField('Work class', choices=workclassChoises, validators=[DataRequired()])

    sex  = RadioField('Sex', choices=[('Male','Male'),('Female','Female')])

    relationshipChoises = [('Husband','Husband'),('Not-in-family','Not-in-family'),('Own-child','Own-child'),
                            ('Unmarried','Unmarried'),('Wife','Wife'),('Other-relative','Other-relative')]
    relationship = SelectField('Relationship status', choices=relationshipChoises, validators=[DataRequired()])

    maritalStatusChoises = [('Married','Married'),('Not-married','Not-married')]
    maritalStatus = SelectField('Marital status', choices=maritalStatusChoises, validators=[DataRequired()])

    #educationChoises = [('Preschool - 9th', 'Preschool - 9th'),('10th - HS-grad', '10th - HS-grad',),
    #                    ('college', 'college'),('Bachelors', 'Bachelors'),('Masters', 'Masters'),
    #                    ('Prof-school', 'Prof-school'),('Doctorate', 'Doctorate')]
    educationChoises = [(5, 'Preschool - 9th'),(9, '10th - HS-grad',),
                        (10, 'college'),(13, 'Bachelors'),(14, 'Masters'),
                        (15, 'Prof-school'),(16, 'Doctorate')]
    education = SelectField('Education', choices=educationChoises, validators=[DataRequired()])

    hoursPerWeek = IntegerField('Hours per week worked. ', validators=[NumberRange(min=1, max=99)])

    submit = SubmitField('Submit')