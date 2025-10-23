from fastapi import FastAPI
from router import userRouter, authRouter
from database import engine
import models

app = FastAPI(title="Python Microservice")

app.include_router(userRouter.router)
app.include_router(authRouter.router)

@app.get("/")
def root():
    return {"status": "Running Successfully ✅"}
