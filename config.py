# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28526237"))
API_HASH = getenv("API_HASH", "936db76a74f9a52cfb2cea8a62e4c20e")
BOT_TOKEN = getenv("BOT_TOKEN", "7780658331:AAFVkysE818mG5NFeK0UiCp_n7a3pNZmnkE")
OWNER_ID = int(getenv("OWNER_ID", "6486192717"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://prisarax:WxuKANYzL5CPyY7d@cluster0.jxlwo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002340322464"))
FORCESUB = getenv("FORCESUB", "blacklumidb")
