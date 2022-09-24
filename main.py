from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/todos")
def get_todos():
    return {
        "success": True,
        "data" : [
            {
                "id" : "1",
                "title" : "coding",
                "completed" : True,
            }
        ]
    }