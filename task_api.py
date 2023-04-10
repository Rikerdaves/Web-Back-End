__license__ = 'GPL, GNU Public License'
__author__ = 'Lady_DMC'

from fastapi import FastAPI, HTTPException, Response, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ['http://localhost:5500', 'http://127.0.0.1:5500']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])

############################################################################################
### Class ###
class Task(BaseModel):
    id: int | None
    descricao: str | None
    responsavel: str | None
    nivel: int 
    prioridade: int
    situacao: str | None

############################################################################################
### ListModel ###
Works: list[Task]=[]

### GET ITEMS ###
@app.get("/tasks")
async def get_items():
    return Works

@app.get("/items/tasks/{work_id}")
async def get_oneitem(work_id: int):
    for item in Works:
        if item.id == work_id:
            return item
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail = f'Item {work_id} não encontrado')

@app.get("/items/tasks/situacao/{work_id}")
async def get_situacao(work_situacao: str):
    return [work_situacao for Works in Task if Works.situacao == work_situacao]

@app.get("/items/tasks/prioridade/{work_id}")
async def get_prioridade(work_prioridade: int):
    return [work_prioridade for Works in Task if Works.prioridade == work_prioridade]

@app.get("/items/tasks/nivel/{work_id}")
async def get_nivel(work_nivel: int):                                                        
    return [work_nivel for Works in Task if Works.nivel == work_nivel]
  
############################################################################################
### POST ITEMS ###

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
async def create_item(work: Task):
    work.id = len(Works) + 1
    Works.append(work)
    return work

############################################################################################
### PUT ITEMS ###

@app.put('/tarefa/atualizar/situacao/{work_id}/emandamento')
def update_emandamento(work_id:int):
    for index in range(len(Task)):
        work_get = Task[index]
        if work_get.id == work_id:
            work_id = work_get
            if work_get.situacao == "Nova" or "Pendente":
                work_get.situacao = "Em Andamento"
                Task[index] = work_get
                return work_get
        
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                        detail= f'not found id={work_id}')

@app.put('/tarefa/atualizar/situacao/{work_id}/pendente')
def update_emandamento(work_id:int):
    for index in range(len(Task)):
        work_get = Task[index]
        if work_get.id == work_id:
            work_id = work_get
            if work_get.situacao == "Nova" or "Em andamento":
                work_get.situacao = "Pendente"
                Task[index] = work_get
                return work_get
        
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                        detail= f'not found id={work_id}')

@app.put('/tarefa/atualizar/situacao/{work_id}/resolvida')
def update_emandamento(work_id:int):
    for index in range(len(Task)):
        work_get = Task[index]
        if work_get.id == work_id:
            work_id = work_get
            if work_get.situacao == "Em andamento":
                work_get.situacao = "Resolvida"
                Task[index] = work_get
                return work_get
        
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                        detail= f'not found id={work_id}')

@app.put('/tarefa/atualizar/situacao/{tarefa_id}/cancelar')
def atualizar_EmAndamento(tarefa_id:int):
    for index in range(len(Task)):
        tarefa_atual = Task[index]
        if tarefa_atual.id == tarefa_id:
            tarefa_id = tarefa_atual
            if tarefa_atual.situacao == "Nova" or "Pendente" or "Em Andamento" and "Resolvida":
                tarefa_atual.situacao = "Cancelada"
                Task[index] = tarefa_atual
                return tarefa_atual
        
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                        detail= f'not found id={tarefa_id}')

@app.put('/tarefa/atualizar/situacao/{work_id}/cancelada/')
def update_emandamento(work_id:int):
    for index in range(len(Task)):
        work_get = Task[index]
        if work_get.id == work_id:
            work_id = work_get
            if work_get.situacao == "Em andamento" or "Pendente" or "Resolvida" and "Nova":
                work_get.situacao = "Cancelada"
                Task[index] = work_get
                return work_get
        
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                        detail= f'not found id={work_id}')

##################################################################################################





             

