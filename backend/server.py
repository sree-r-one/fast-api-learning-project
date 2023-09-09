# region IMPORT
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models import Post

# endregion IMPORT

app = FastAPI()

origins = ["https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.post("/create")
async def root(post: Post):
    return {"message": post}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
