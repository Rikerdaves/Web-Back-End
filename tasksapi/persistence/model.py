from pydantic import BaseModel

class Document(BaseModel):
    descricao: str | None
    responsavel: str | None
    nivel: int 
    prioridade: int
    situacao: str | None




     