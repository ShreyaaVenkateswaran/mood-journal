# tests/test_api.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
from app import JournalEntry

def test_post_entry(client):
    res = client.post('/entries', json={
        "date": "2025-06-20",
        "mood": "Happy",
        "note": "Feeling good"
    })
    assert res.status_code == 201
    assert res.json['message'] == "Entry added successfully"

def test_get_entries(client):
    res = client.get('/entries')
    assert res.status_code == 200
    assert isinstance(res.json, list)

def test_put_entry(client):
    client.post('/entries', json={"date": "2025-06-20", "mood": "Sad", "note": "Bad day"})
    res = client.put('/entries/1', json={"mood": "Okay", "note": "Better now"})
    assert res.status_code == 200
    assert res.json['message'] == "Entry updated"

def test_delete_entry(client):
    client.post('/entries', json={"date": "2025-06-20", "mood": "Neutral", "note": "Fine"})
    res = client.delete('/entries/1')
    assert res.status_code == 200
    assert res.json['message'] == "Entry deleted"
