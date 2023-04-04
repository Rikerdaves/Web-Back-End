from presentation.db import db

def create_document(collection, document):
    result = db[collection].insert_one(document)
    return str(result.inserted_id)

def read_document(collection, filter={}):
    result = db[collection].find(filter)
    documents = [doc for doc in result]
    return documents

def update_document(collection, filter, update):
    result = db[collection].update_many(filter, update)
    return result.modified_count

def delete_document(collection, filter):
    result = db[collection].delete_many(filter)
    return result.deleted_count

