from typing import TypedDict

from bson.objectid import ObjectId
from pymongo import MongoClient

from presentation.model import Document

class DocumentMongo(TypedDict):
    _id: ObjectId
    descricao: str 
    responsavel: str 
    nivel: int 
    prioridade: int
    situacao: str 


class DocumentMongoDBRepository():
    def __init__(self):
        client = MongoClient("mongodb+srv://ladydmc:devilmaycry5@apiserver.lcs3qz2.mongodb.net/?retryWrites=true&w=majority")
        db = client["apiserver"]
        self.document = db["documents"]
        try:
            print('MongoDB 💖')
        except Exception:
            print('ERROR!')

    def all(self, skip=0, take=0):
        documents = self.document.find().skip(skip).limit(take)
        return list(map(Document.fromDict, documents))

    def Save(self, document):
        _id = self.document.insert_one(document.toDict()).inserted_id
        document.id = str(_id)
        return document

    def get_one(self, document_id):
        filtro = {"_id": ObjectId(document_id)}
        document_find = self.document.find_one(filtro)
        return Document.fromDict(document_find) if document_find else None

    def delete(self, document_id):
        filtro = {"_id": ObjectId(document_id)}
        self.document.delete_one(filtro)

    def update(self, document_id, document):
        filtro = {"_id": ObjectId(document_id)}
        self.document.update_one(filtro, {'$set': document.toDict()})
        document.id = document_id
        return document        



    






