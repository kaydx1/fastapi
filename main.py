from fastapi import FastAPI
from lib.counter import get_counter, increase_counter

app = FastAPI()

@app.get("/api/counter")
async def read() -> int:
    return get_counter()

@app.post("/api/counter")
async def count() -> int:
    return increase_counter()