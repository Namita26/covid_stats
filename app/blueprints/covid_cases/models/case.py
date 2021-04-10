from mongoengine import Document, StringField, IntField, EmbeddedDocumentField, DateTimeField, DateField

from app.utils.base_models import CustomDocument, BaseQuerySet
from app.utils.signal_handler import update_created_modified
from app.blueprints.covid_cases.models.location import Location


STATUSES = ["ACTIVE", "RECOVERED", "DECEASED"]


@update_created_modified.apply
class Case(Document, CustomDocument):
    """
    Model for a Covid Case
    """

    user_id = IntField(unique_with='current_status')
    current_status = StringField(choices=STATUSES)
    location = EmbeddedDocumentField(Location)

    # Dates
    found_active_on = DateField()
    recovered_on = DateField()
    deceased_on = DateField()

    # Created / Modified
    created_at = DateTimeField()
    modified_at = DateTimeField()

    meta = {
        'queryset_class': BaseQuerySet
    }

