import json

from mongoengine import QuerySet


class BaseQuerySet(QuerySet):

    def to_json_dict(self):
        return [obj.to_json_dict() for obj in self]

    def to_json(self):
        return json.dumps(self.to_json_dict(), default=str)


class CustomDocument:

    def to_json_dict(self):
        return self.to_mongo().to_dict()

    def to_json(self):
        return json.dumps(self.to_json_dict(), default=str)
