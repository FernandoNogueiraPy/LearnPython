from src.repositories import mongo_connection
from src.config import DATABASE, COLLECTION_CHALLENGE_OVERVIEW
from src.entities.challenges.challenge_overview import ChallengeOverview

if not DATABASE or not COLLECTION_CHALLENGE_OVERVIEW:
    raise Exception("""
                    
        You need to set the environment variables: 
        MONGO_CONNECTION and DATABASE and COLLECTION_CHALLENGE_OVERVIEW
        
        """)


respository_challenge_overview_async = mongo_connection.async_client(
    database_name=DATABASE,
    collection_name=COLLECTION_CHALLENGE_OVERVIEW,
    model=ChallengeOverview,
)


respository_challenge_overview_sync = mongo_connection.sync_client(
    database_name=DATABASE,
    collection_name=COLLECTION_CHALLENGE_OVERVIEW,
    model=ChallengeOverview,
)
