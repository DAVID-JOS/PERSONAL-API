from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup tasks (e.g., DB connections) go here
    yield
    # Shutdown tasks go here

app = FastAPI(
    title="Clean API",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/health", tags=["system"])
async def health():
    return {"status": "ok"}

@app.get("/", tags=["system"])
async def root():
    return {"message": "API is running"}

@app.post("/v1/echo", tags=["demo"])
async def echo(payload: dict):
    return {"received": payload}

@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error", "detail": str(exc)},
  )
  
