from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from presentation.controllers import document_controller, user_controller
from presentation.log_middleware import LogMiddleware

import uvicorn

app = FastAPI()

origins = ['http://localhost:5500',
           'http://127.0.0.1:5500',
           'https://127.0.0.1:8000',
           'http://0.0.0.0:8000',
           'https://tarefasapi-u4ir.onrender.com/document']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])

app.add_middleware(LogMiddleware)                   

# Rotas e Controllers
app.include_router(document_controller.routes,
                   prefix=document_controller.prefix)
app.include_router(user_controller.routes,
                   prefix=user_controller.prefix)

if __name__ == '__main__':
    app = application = uvicorn.run(app.app, host='0.0.0.0', port=8000)
