import pytest
from src.handlers import process_event
from src.models import Event

def test_process_event():
    event = Event(data='hello')
    response = process_event(event)
    assert response.result == 'HELLO'