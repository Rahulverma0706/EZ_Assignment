from fastapi import FastAPI
from routers import auth
from routers import files

app = FastAPI()
app.include_router(files.router)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "Welcome to the Secure File Sharing API"}
