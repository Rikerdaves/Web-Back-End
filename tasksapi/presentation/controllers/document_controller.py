from fastapi import APIRouter, HTTPException, status

from persistence.db_repository import DocumentMongoDBRepository

from ..model import Document

print('Controller OK✅')
routes = APIRouter()
prefix = '/document'

document_repository = DocumentMongoDBRepository()


@routes.get('/')
def all(skip: int | None = 0, take: int | None = 0):
    return document_repository.all(skip, take)


@routes.get('/{document_id}')
def get_one(document_id: int | str):
    document = document_repository.get_one(document_id)

    # fail fast
    if not document:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Not found item with id = {document_id }')

    return document


@routes.post('/', status_code=status.HTTP_201_CREATED)
def new_document(document: Document):
    return document_repository.salvar(document)


@routes.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(document_id: int | str):
    document = document_repository.get_one(document_id)

    if not document:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Not Found")

    document_repository.remover(document_id)


@routes.put('/{document_id}', status_code=status.HTTP_200_OK)
def update(document_id: int | str, document: Document):
    document_repository.get_one(document_id)

    return document_repository.update(document_id, document)

