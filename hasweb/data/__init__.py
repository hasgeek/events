from hasweb import models

models.db.create_all()
models.db.session.add(models.Event(title="Hello"))
models.db.session.add(models.Event(title="World"))
models.db.session.add(models.Event(title="!"))
models.db.session.commit()
