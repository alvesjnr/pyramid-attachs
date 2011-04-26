from isis import model


class Entry(model.CouchdbDocument):
    title = model.TextProperty()
    attachment = model.TextProperty()
    description = model.TextProperty()

