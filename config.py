## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu6tbLUCYGhlMuaTJx0JeRRmI4REqPzj86dmJwXAn7JcDQax-5uiG9EzyA4d6zLohclWgZ1LX9b-Y0GLY1MK0rUIz1mmg4cnDHkYDhckTkWHqQNDiXkyTt_UhxVkSRhwgmMQlQU-uFsd8RISAP74-jW2WbHnny7uUiRAaFOE9lR_bB9-fxNSbYsmnxfups5nPtR9i12r-noAKjaAiBMAbSC7yDn4o01wKsYqSax-F39_vrAbmGRQ0c9qo3Fb-pQa0lTUd8Fe-oDfjAEpOviFcXBa5ebQHL4eSNTmD4ZGzVsjOKZqjQL2g269yExn0jIp3Ul4V2x2leKEIkWC4huOAdhk=")
BOT_TOKEN = getenv("BOT_TOKEN", "5489011548:AAHhkd1ekUBtwiPVfCkUuHlss2n8qk_lEvE")
BOT_NAME = getenv("BOT_NAME", "Iraq¹ music")
API_ID = int(getenv("API_ID", "9982246"))
API_HASH = getenv("API_HASH", "4c9bd38e49d20838b6d180428f883499")
OWNER_NAME = getenv("OWNER_NAME", "آلبآريـﮯ")
OWNER_USERNAME = getenv("OWNER_USERNAME", "YF_YU")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "mosegabot")
OWNER_ID = getenv("OWNER_ID", "1346025095")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "FATO_10")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "FF_5unnm")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "FF_5unnm")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
