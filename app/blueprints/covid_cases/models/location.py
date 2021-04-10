from mongoengine import StringField, EmbeddedDocument, PointField


class Location(EmbeddedDocument):

    area = StringField(required=True)
    city = StringField(required=True)
    state = StringField(required=True)
    country = StringField(required=True)
    continent = StringField(required=True)
