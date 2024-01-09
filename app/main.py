from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import user, role, user_roles

app = FastAPI()

origins = ['*'] 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']

)

app.include_router(user.router)
app.include_router(role.router)
app.include_router(user_roles.router)

@app.get("/") 
def root():
    return {'version': '0.0.1'}
              