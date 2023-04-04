from persistence.crud import create_document, read_document, update_document, delete_document
from persistence.model import Document
from fastapi import FastAPI, HTTPException
from bson import ObjectId

app = FastAPI()

@app.post("/documents/")
def create_document_handler(document: Document):
    document_dict = document.dict()
    document_id = create_document("documents", document_dict)
    return {"document_id": document_id}

@app.get("/documents/")
def read_documents():
    documents = read_document("documents")
    result = []
    for doc in documents:
        doc["_id"] = str(doc["_id"])
        result.append(doc)
    return result

@app.put("/documents/{document_id}")
def update_document(document_id: str, document: Document):
    document_dict = document.dict()
    filter = {"_id": ObjectId(document_id)}
    update = {"$set": document_dict}
    modified_count = update_document("documents", filter, update)
    if modified_count == 0:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"document_id": document_id}

@app.delete("/documents/{document_id}")
def delete_document(document_id: str):
    filter = {"_id": ObjectId(document_id)}
    deleted_count = delete_document("documents", filter)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"document_id": document_id}
