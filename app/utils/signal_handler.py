from datetime import datetime

from mongoengine import signals


def handler(event):
    """Signal decorator to allow use of callback functions as class decorators."""

    def decorator(fn):
        def apply(cls):
            event.connect(fn, sender=cls)
            return cls

        fn.apply = apply
        return fn

    return decorator


@handler(signals.pre_save)
def update_created_modified(sender, document):
    current_datetime = datetime.utcnow()
    document.modified_at = current_datetime

    if not document.found_active_on:
        document.found_active_on = current_datetime

    if not document.created_at:
        document.created_at = current_datetime
