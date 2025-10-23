from fastapi import FastAPI
from router import userRouter, authRouter
from fastapi.middleware.cors import CORSMiddleware
from rateLimiter import limiter
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

app = FastAPI(title="Python Microservice")

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

origins = ["http://localhost:5173"]

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
