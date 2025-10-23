from fastapi import FastAPI
from router import userRouter, authRouter
from database import engine
import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Python Microservice")

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(authRouter.router)
app.include_router(userRouter.router)

@app.get("/")
def root():
    return {"status": "Running Successfully ✅"}
