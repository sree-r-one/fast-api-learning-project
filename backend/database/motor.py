# region IMPORT
import motor.motor_asyncio

# endregion IMPORT


async def connect_to_mongodb():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["SBOOK_DB"]
    return db
