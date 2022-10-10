import motor.motor_asyncio
from pymongo import MongoClient
from app.core.config import MONGODB_URL

# Async Connection

async_client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
async_database = async_client.climate_fieldview_db

dominios_collection = async_database.get_collection("dominios_collection")
error_codes_collection = async_database.get_collection("error_codes_collection")

# Sync Connection

sync_client = MongoClient(MONGODB_URL)
sync_database = sync_client.climate_fieldview_db

error_codes_collection_sync = sync_database.get_collection("error_codes_collection")