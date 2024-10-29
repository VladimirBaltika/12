from flask import Flask, render_template, request, redirect, url_for
from models import db, Note

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    notes = Note.query.all()
    return render_template('index.html',notes=notes)

@app.route('/add_note', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        name = request.form['name']
        new_note = Note(name=name)
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_note.html')
    


if __name__ == '__main__':
    app.run(debug=True)
