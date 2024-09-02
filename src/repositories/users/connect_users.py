from src.repositories import mongo_connection
from src.config import DATABASE, COLLECTION_USERS
from src.entities.users.login_user import LoginUser

if not DATABASE or not COLLECTION_USERS:
    raise Exception("""
                    
        You need to set the environment variables: 
        MONGO_CONNECTION and DATABASE and COLLECTION_USERS
        
        """)


respository_users_async = mongo_connection.async_client(
    database_name=DATABASE,
    collection_name=COLLECTION_USERS,
    model=LoginUser,
)


respository_users_sync = mongo_connection.sync_client(
    database_name=DATABASE,
    collection_name=COLLECTION_USERS,
    model=LoginUser,
)
