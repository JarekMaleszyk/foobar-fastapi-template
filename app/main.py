import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, user, role, user_roles, foo, bar

app = FastAPI(
    title="FastAPI Template",
    description="Template project using python FastAPI framework.",
    version="0.1.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']

)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(role.router)
app.include_router(user_roles.router)
app.include_router(foo.router)
app.include_router(bar.router)

             
if __name__ == "__main__":
    print("Navigate the url: http://localhost:8000/docs for Swagger docs.")
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True, workers=2)