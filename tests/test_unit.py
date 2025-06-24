# tests/test_unit.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
from app import JournalEntry

def test_journal_entry_to_dict():
    entry = JournalEntry(id=1, date="2025-06-20", mood="Happy", note="Test")
    result = entry.to_dict()
    assert result == {
        "id": 1,
        "date": "2025-06-20",
        "mood": "Happy",
        "note": "Test"
    }
