from flask import Flask, request, Response, render_template
from flask_wtf import FlaskForm
from wtforms import FileField


from flask_uploads import configure_uploads, IMAGES, UploadSet
import os

from db import db_init, db


app = Flask(__name__)
# SQLAlchemy config. Read more: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

class FileContents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)
    mimetype = db.Column(db.Text, nullable=False)


SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOADED_IMAGES_DEST'] =  './images'
  
images = UploadSet('images', IMAGES)
configure_uploads(app, images)
class MyForm(FlaskForm):
    image = FileField('image')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm() 

    if request.method == "POST":
        filename = images.save(form.image.data)
        return F'Filename: {filename}'

    return render_template('index.html', form=form)


app.run(host='127.0.0.1', port=4000)


