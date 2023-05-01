from fastapi import APIRouter

routes = APIRouter()
prefix = '/usuarios'

print('User Controller OK✅')

@routes.get('/')
def todos_usuario():
    return []