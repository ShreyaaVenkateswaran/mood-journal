# Calendar Mood Board (Mood Journal)

A full-stack mood journaling application that allows users to log and visualize their daily moods on a calendar interface. The project includes a Flask-based RESTful API, a MySQL database, and a simple HTML/CSS/JS frontend rendered via Flask.

---

### Features

- Add, view, update, and delete daily mood entries
- Display moods and notes in a monthly calendar view
- RESTful API for backend operations
- Uses MySQL for persistent storage

---

### API Endpoints & Their Functionality

| Method | Endpoint             | Description                           |
|--------|----------------------|---------------------------------------|
| GET    | `/entries`           | Retrieve all mood entries             |
| POST   | `/entries`           | Create a new mood entry               |
| PUT    | `/entries/<int:id>`  | Update an existing mood entry by ID   |
| DELETE | `/entries/<int:id>`  | Delete a mood entry by ID             |

### Sample Request/Response

#### `POST /entries`

*Request:*
{
  "date": "2025-06-20",
  "mood": "Happy",
  "note": "Had a great day!"
}

*Response*
{
  "message": "Entry added successfully"
}

#### 'GET /entries'
*Response*
[
  {
    "id": 1,
    "date": "2025-06-20",
    "mood": "Happy",
    "note": "Had a great day!"
  }
]

### Database Used

- **Database**: MySQL  
- **Integration**: SQLAlchemy (ORM) using `pymysql` driver

---

### Sample Schema

CREATE TABLE journal_entry (
  id INT PRIMARY KEY AUTO_INCREMENT,
  date VARCHAR(10) NOT NULL,
  mood TEXT,
  note TEXT
);

### Integration in Flask (app.py)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yourpassword@localhost/moodjournal'
db = SQLAlchemy(app)

### How to Run the Server
#### Prerequisites
Python 3.8+
MySQL Server (e.g., XAMPP, WAMP, or standalone)

#### Install dependencies:
pip install Flask Flask-SQLAlchemy flask-cors pymysql

#### Setup MySQL
Create a database:
CREATE DATABASE moodjournal;
Update your app.py with your MySQL credentials.

#### Start the Flask Server
From the root project directory, run:
python backend/app.py

Server will start at:
http://localhost:5000

### How to Run the Frontend Locally
The frontend (index.html) is served automatically by Flask.

Open your browser and visit:
http://localhost:5000

#### You can:
Add a new mood entry
View entries for each day in a calendar
Edit or delete existing entries

### How to Interact with the API
#### Add an Entry
curl -X POST http://localhost:5000/entries \
  -H "Content-Type: application/json" \
  -d '{"date":"2025-06-20","mood":"Relaxed","note":"Watched a movie"}'
  
#### Get All Entries
curl http://localhost:5000/entries

#### Update an Entry
curl -X PUT http://localhost:5000/entries/1 \
  -H "Content-Type: application/json" \
  -d '{"date":"2025-06-20","mood":"Excited","note":"Updated note"}'
  
#### Delete an Entry
curl -X DELETE http://localhost:5000/entries/1
