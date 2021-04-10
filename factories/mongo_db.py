from mongoengine import connect


def setup_mongo_db(app):
    return connect(host=app.config['MONGO_DB_URL'], connect=False)
