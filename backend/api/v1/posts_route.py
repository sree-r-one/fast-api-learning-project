# region IMPORT
from fastapi import APIRouter, Response, status, HTTPException, Depends
from database import connect_to_mongodb
from models import Post
import motor.motor_asyncio as mot
from bson import ObjectId

# endregion IMPORT

router = APIRouter(prefix="/api/v1/posts", tags=["posts"])


# Get
@router.get("/")
async def get_posts():
    return {"message": "Hello"}


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_post(id: str, client: mot.AsyncIOMotorClient = Depends(connect_to_mongodb)):
    # Find Collection
    collection = client["posts"]
    # Find Document
    post = await collection.find_one({"_id": ObjectId(id)})

    if post:
        post.pop("_id")  # Remove _id from dict
        return {"message": dict(post)}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")


# Create
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post, client: mot.AsyncIOMotorClient = Depends(connect_to_mongodb)):
    try:
        collection = client["posts"]
        result = await collection.insert_one(dict(post))
        print(result.inserted_id)
        return {"message": str(result.inserted_id)}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# Update
@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_post(id: int):
    return {"message": "Hello"}


# Delete
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    return {"message": "Hello"}
