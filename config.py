from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "25276967"
# -------------------------------------------------------------
API_HASH = "daf793293a5a244e5c426a129656e0a1"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7446465090"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/THE-VIP-BOY-OP/VIP-CHATBOT")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
SUPPORT_GRP = "TG_FRIENDSS"
UPDATE_CHNL = "VIP_CREATORS"
OWNER_USERNAME = "THE_VIP_BOY"
# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", None)
    
