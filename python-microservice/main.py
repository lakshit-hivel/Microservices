from fastapi import FastAPI
from router import userRouter
from database import engine
import models

app = FastAPI(title="Python Microservice")

app.include_router(userRouter.router)

@app.get("/")
def root():
    return {"status": "Running Successfully ✅"}
