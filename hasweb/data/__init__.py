from hasweb import models

models.db.create_all()
models.db.session.add(models.Event(title="Hello"))
models.db.session.add(models.Event(title="World"))
models.db.session.add(models.Event(title="!"))
models.db.session.commit()


MAP_TYPES = {
    'leaflet': models.MapType(id='leaflet', name='Leaflet'),
    'mapbox': models.MapType(id='mapbox', name='Mapbox')
}

EVENT_TYPES = [
    models.EventType(id='conference', name='Conference'),
    models.EventType(id='workshop', name='Workshop')
]
