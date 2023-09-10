# region IMPORT
from fastapi import APIRouter, Response, status, HTTPException, Depends
from database import connect_to_mongodb
from models import Post
import motor.motor_asyncio as mot

# endregion IMPORT

router = APIRouter(prefix="/api/v1/posts", tags=["posts"])


# Get
@router.get("/")
async def get_posts():
    return {"message": "Hello"}


@router.get("/{id}")
async def get_post(id: int):
    return {"message": "Hello"}


# Create
@router.post("/")
async def create_post(post: Post, client: mot.AsyncIOMotorClient = Depends(connect_to_mongodb)):
    try:
        collection = client["posts"]
        result = await collection.insert_one(dict(post))
        print(result.inserted_id)
        return {"message": str(result.inserted_id)}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# Update
@router.put("/{id}")
async def update_post(id: int):
    return {"message": "Hello"}


# Delete
@router.delete("/{id}")
async def delete_post(id: int):
    return {"message": "Hello"}
