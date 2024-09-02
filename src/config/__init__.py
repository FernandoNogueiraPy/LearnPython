from dotenv import load_dotenv
from os import getenv

load_dotenv()


URL_MONGO = getenv("URL_MONGO")
DATABASE = getenv("DATABASE")
COLLECTION_USERS = getenv("COLLECTION_USERS")

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
