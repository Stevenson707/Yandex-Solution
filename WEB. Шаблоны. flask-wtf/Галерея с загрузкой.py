import os
from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired


app = Flask(__name__)
secret_key = os.getenv('SECRET_KEY')
app.config['SECRET_KEY'] = str(secret_key)


def get_image_paths(base_path):
    # пути относительно static
    return [f"img/gallery/{i}" for i in os.listdir(base_path)]


class GalleryForm(FlaskForm):
    photo = FileField('Добавить картинку', validators=[DataRequired()])
    submit = SubmitField('Загрузить')


@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    image_base_path = 'static/img/gallery'
    if request.method == 'GET':
        form = GalleryForm()
        image_paths = get_image_paths(image_base_path)
        return render_template('gallery.html', image_paths=image_paths, form=form)
    elif request.method == 'POST':
        file = request.files['photo']
        with open(os.path.join(image_base_path, file.filename), 'wb') as f:
            f.write(file.stream.read())
        return redirect('/gallery')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
