def process_event(event: Event) -> Response:
    # Lógica de procesamiento del evento
    processed_data = event.data.upper()
    return Response(result=processed_data)