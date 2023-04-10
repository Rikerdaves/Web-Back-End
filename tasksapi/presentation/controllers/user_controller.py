from fastapi import APIRouter

routes = APIRouter()
prefix = '/usuarios'

print('User Controller ✅')


@routes.get('/')
def todos_usuario():
    return []