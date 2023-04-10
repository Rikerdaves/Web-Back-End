from pydantic import BaseModel
from bson.objectid import ObjectId

class Document(BaseModel):
    descricao: str | None
    responsavel: str | None
    nivel: int 
    prioridade: int
    situacao: str | None

    class Config:
        orm_mode = True

    @classmethod
    def fromDict(cls, document):
        document_ = Document(id=str(document['_id']),
                       descricao = document['descricao'],
                       responsavel = document['responsavel'],
                       nivel = document['nivel'],
                       prioridade = document['prioridade'],
                       situacao= document['situacao'])
        return document_

    def toDict(self):
        return {
            "nome": self.nome,
            "genero": self.genero,
            "duracao": self.duracao,
            "ano": self.ano
        }


class User(BaseModel):
    id: int | None
    descricao: str | None
    responsavel: str
    nivel: int
    prioridade: int
    situacao: str | None




     