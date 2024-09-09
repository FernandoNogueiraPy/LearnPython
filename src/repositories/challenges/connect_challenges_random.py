from src.repositories import mongo_connection
from src.config import COLLECTION_CHALLENGES_RANDOM, DATABASE
from src.entities.challenges.challenge import ChallengeRandom

if not DATABASE or not COLLECTION_CHALLENGES_RANDOM:
    raise Exception("""
                    
        You need to set the environment variables: 
        MONGO_CONNECTION and DATABASE and COLLECTION_CHALLENGES_RANDOM_RANDOM
        
        """)


respository_challenge_random_async = mongo_connection.async_client(
    database_name=DATABASE,
    collection_name=COLLECTION_CHALLENGES_RANDOM,
    model=ChallengeRandom,
)


respository_challenge_random_sync = mongo_connection.sync_client(
    database_name=DATABASE,
    collection_name=COLLECTION_CHALLENGES_RANDOM,
    model=ChallengeRandom,
)
