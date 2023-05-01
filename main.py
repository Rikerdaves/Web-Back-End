from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from presentation.controllers import document_controller, user_controller

app = FastAPI()

origins = ['http://localhost:5500',
           'http://127.0.0.1:5500',
           'https://127.0.0.1:8000',
           'http://0.0.0.0:8000',
           'https://tarefasapi-u4ir.onrender.com']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])

# Rotas e Controllers
app.include_router(document_controller.routes,
                   prefix=document_controller.prefix)
app.include_router(user_controller.routes,
                   prefix=user_controller.prefix)