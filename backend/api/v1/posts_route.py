# region IMPORT
from fastapi import APIRouter, Response, status, HTTPException

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
async def create_post():
    return {"message": "Hello"}


# Update
@router.put("/{id}")
async def update_post(id: int):
    return {"message": "Hello"}


# Delete
@router.delete("/{id}")
async def delete_post(id: int):
    return {"message": "Hello"}
