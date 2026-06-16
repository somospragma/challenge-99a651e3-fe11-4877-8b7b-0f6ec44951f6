import os
from src.handlers import process_event
from src.models import Event, Response

def lambda_handler(event, context):
    try:
        event_obj = Event(**event)
        response = process_event(event_obj)
        return response.dict()
    except Exception as e:
        print(f'Error: {e}')
        return {'error': str(e)}