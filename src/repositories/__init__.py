from addemongo import MongoConnection
from src.config import URL_MONGO

if not URL_MONGO:
    raise Exception("""
                    
        You need to set the environment variables: 
        URL_MONGO
        
        """)


mongo_connection = MongoConnection(
    host=URL_MONGO,
    ssl=True,
    tlsAllowInvalidCertificates=True,
)
