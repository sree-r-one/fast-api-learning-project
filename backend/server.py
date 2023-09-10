# region IMPORT
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models import Post
from database import connect_to_mongodb
import api.v1.posts_route as posts_route

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
app.include_router(posts_route.router)


# region START AND SHUTDOWN
@app.on_event("startup")
async def startup_event():
    print("Starting up...")
    app.mongodb_client = await connect_to_mongodb()


@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down...")
    app.mongodb_client.close()


# endregion START AND SHUTDOWN


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
