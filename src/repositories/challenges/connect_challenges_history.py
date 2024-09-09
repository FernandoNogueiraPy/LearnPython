from src.repositories import mongo_connection
from src.config import DATABASE, COLLECTION_CHALLENGES_HISTORY
from src.entities.challenges.challenge import Challenge

if not DATABASE or not COLLECTION_CHALLENGES_HISTORY:
    raise Exception("""
                    
        You need to set the environment variables: 
        MONGO_CONNECTION and DATABASE and COLLECTION_CHALLENGES_HISTORY
        
        """)


respository_challenge_history_async = mongo_connection.async_client(
    database_name=DATABASE,
    collection_name=COLLECTION_CHALLENGES_HISTORY,
    model=Challenge,
)


respository_challenge_history_sync = mongo_connection.sync_client(
    database_name=DATABASE,
    collection_name=COLLECTION_CHALLENGES_HISTORY,
    model=Challenge,
)
