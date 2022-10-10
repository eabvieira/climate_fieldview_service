from app.db.mongo import error_codes_collection_sync


def get_all_error_codes():

    cursor = error_codes_collection_sync.find({'dominio': 'error_codes'}, {"_id": 0})

    return [items for items in cursor]
