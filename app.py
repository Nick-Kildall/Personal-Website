from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Creating Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "Super Secret Key... I should hide this later"

### Create Form Class
class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Route Decorator
@app.route('/')
def index():
    return render_template("index.html")


# Form testing page
@app.route('/name', methods = ['GET', 'POST'])
def name():
    name = None
    nform = NameForm()
    if nform.validate_on_submit():
        name = nform.name.data
        nform.name.data = ""
    return render_template("name.html", 
        name = name, 
        form = nform) 

# Invalid URL
@app.errorhandler(404)
def page_not_found(e): 
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e): 
    return render_template("404.html"), 500


