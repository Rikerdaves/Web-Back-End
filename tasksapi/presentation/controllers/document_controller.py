from fastapi import APIRouter, HTTPException, status

from persistence.db_repository import DocumentMongoDBRepository



from ..model import Document

print('Controller ✅')
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
                            detail=f'Não há filme com id = {document_id }')

    return document


@routes.post('/', status_code=status.HTTP_201_CREATED)
def new_document(document: Document):
    return document_repository.salvar(document)


@routes.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(document_id: int | str):
    document = document_repository.get_one(document_id)

    if not document:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Filme não encontrado")

    document_repository.remover(document_id)


@routes.put('/{document_id}')
def update(document_id: int | str, document: Document):
    document_find = document_repository.get_one(document_id)

    if not document_find:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Filme não encontrado")

    return document_repository.atualizar(document_id, document)