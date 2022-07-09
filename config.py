## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
if str(getenv("SESSION_NAME")).strip() == "":
    SESSION_NAME = str(None)
else:
    SESSION_NAME = str(getenv("SESSION_NAME"))

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5445662870:AAFZVOm6XDVRnpNfsXZxyVdFJK_D_YX8sLo")
BOT_NAME = getenv("BOT_NAME", "༺⚚亗അറുമുഖൻ亗⚚༻ᵇᵒᵗ")

API_ID = int(getenv("API_ID", "19921548"))
API_HASH = getenv("API_HASH", "d2d8457cdec9673de82c46b4da6b9469")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "𒀱ꪳ𖤓࿈കൃഷ്ണതുളസ᭄🌙⸙ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ࿈𖤓𒀱ꪳ")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Krishnadreamgirl")
ALIVE_NAME = getenv("ALIVE_NAME", "༺⚚亗അറുമുഖൻ亗⚚༻ᵇᵒᵗ")
BOT_USERNAME = getenv("BOT_USERNAME", "Arumughan_MusicBot")
OWNER_ID = getenv("OWNER_ID", "5555502929")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Geethika_MV")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "kk_kovilakam")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "KANTHARI_WRITINGS")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5007155069").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/be09b1c34685e37cf942e.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/2bdde63c977aac09fc639.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
