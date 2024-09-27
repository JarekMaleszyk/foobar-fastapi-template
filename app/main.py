from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, user, role, user_roles, foo, bar


app = FastAPI()

all = ['*'] 
app.add_middleware(
    CORSMiddleware,
    allow_origins=all,
    allow_credentials=True,
    allow_methods=all,
    allow_headers=all

)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(role.router)
app.include_router(user_roles.router)
app.include_router(foo.router)
app.include_router(bar.router)

@app.get('/') 
def root():
    return {'version': '0.0.2 - Ubuntu 12'}
             
