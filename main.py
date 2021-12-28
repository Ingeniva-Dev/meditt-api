from typing import Optional
from fastapi import FastAPI


@app.get("/")
def root():
    return {"message": "hello its my api"}