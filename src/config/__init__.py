from dotenv import load_dotenv
from os import getenv

load_dotenv()


URL_MONGO = getenv("URL_MONGO")
DATABASE = getenv("DATABASE")
COLLECTION_USERS = getenv("COLLECTION_USERS")
COLLECTION_CHALLENGE_OVERVIEW = getenv("COLLECTION_CHALLENGE_OVERVIEW")

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
