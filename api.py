__license__ = 'GPL, GNU Public License'
__author__ = 'Rikerdaves'

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

### Class ###
class Task(BaseModel):
    id: int | None
    descricao: str 
    responsavel: str | None
    nivel: int 
    prioridade: int
    situacao: str | None

### ListModel ###
Works: list[Task]=[]

##### CRUD #####

###Get tasks ###
@app.get("/tasks")
async def get_all(skip: int | None = None, limit: int | None = None):
    start = skip

    if skip and limit:
        finish = skip + limit
    else:
        finish = None

    return Works[start:finish]


@app.get("/tasks/{work_id}")
async def get_one(work_id: int):
    for work in Works:
        if work.id == work_id:
            return work

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail = f'Not Found id = {work_id}')

@app.get('/tarefas/situacao/{work_situacao}')
async def get_situacao(work_situacao: str):
    return [work_situacao for Works in Task if Works.situacao == work_situacao]

@app.get('/tarefas/situacao/{work_nivel}')
async def get_situacao(work_nivel: int):
    return [work_nivel for Works in Task if Works.nivel == work_nivel]

@app.get('/tarefas/situacao/{work_prioridade}')
async def get_situacao(work_prioridade: int):
    return [work_prioridade for Works in Task if Works.prioridade == work_prioridade]    
                           
### Post tasks ###
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
async def create_new(work: Task):
    work.id = len(Works) + 0
    Works.append(work)
    return work

### Put tasks ###
@app.put("/tasks/{work_id}")
async def update_one(work_id: int, work: Task):
    for index in range(len(Works)):
        work = Works[index]
        if work.id == work_id:
            work.id = work_id
            Works[index] = work
            return work

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail = f'Not Found id = {work_id}')
                                    
### Delete tasks ###
@app.delete("/tasks/{work_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(work_id: int):
    for work in Works:
        if work.id == work_id:
            Works.remove(work)
        return

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail= f'Not Found id = {work_id}')



    

            
    


       
            

