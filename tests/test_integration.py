import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
from app import db, JournalEntry

def test_create_and_fetch_entry(client):
    # Insert entry using db directly
    with client.application.app_context():
        entry = JournalEntry(date="2025-06-21", mood="Sad", note="Not great")
        db.session.add(entry)
        db.session.commit()

        # Query back and assert
        fetched = JournalEntry.query.filter_by(date="2025-06-21").first()
        assert fetched is not None
        assert fetched.mood == "Sad"