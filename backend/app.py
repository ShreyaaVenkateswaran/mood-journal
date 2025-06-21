from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os

# Correctly define the path to templates
template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'templates')
static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static')
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Krishna3*@localhost/moodjournal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    mood = db.Column(db.Text, nullable=True)
    note = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'mood': self.mood,
            'note': self.note
        }

with app.app_context():
    db.create_all()

@app.route('/entries', methods=['GET'])
def get_entries():
    entries = JournalEntry.query.all()
    return jsonify([entry.to_dict() for entry in entries])

@app.route('/entries', methods=['POST'])
def add_entry():
    data = request.get_json()
    new_entry = JournalEntry(
        date=data['date'],
        mood=data['mood'],
        note=data.get('note', '')
    )
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({'message': 'Entry added successfully'}), 201

@app.route('/entries/<int:id>', methods=['PUT'])
def update_entry(id):
    data = request.get_json()
    entry = JournalEntry.query.get_or_404(id)
    entry.mood = data['mood']
    entry.note = data['note']
    db.session.commit()
    return jsonify({'message': 'Entry updated'})

@app.route('/entries/<int:id>', methods=['DELETE'])
def delete_entry(id):
    entry = JournalEntry.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    return jsonify({'message': 'Entry deleted'})

@app.route('/')
def serve_frontend():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
