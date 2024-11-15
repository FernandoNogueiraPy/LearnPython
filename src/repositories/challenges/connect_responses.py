from src.repositories import mongo_connection
from src.config import DATABASE, COLLECTION_CHALLENGES_RESPONSE
from src.entities.challenges.challenge_response import ResponseChallengeCorrect

if not DATABASE or not COLLECTION_CHALLENGES_RESPONSE:
    raise Exception("""
                    
        You need to set the environment variables: 
        MONGO_CONNECTION and DATABASE and COLLECTION_CHALLENGES_RESPONSE
        
        """)


respository_challenge_response_async = mongo_connection.async_client(
    database_name=DATABASE,
    collection_name=COLLECTION_CHALLENGES_RESPONSE,
    model=ResponseChallengeCorrect,
)


respository_challenge_response_sync = mongo_connection.sync_client(
    database_name=DATABASE,
    collection_name=COLLECTION_CHALLENGES_RESPONSE,
    model=ResponseChallengeCorrect,
)
