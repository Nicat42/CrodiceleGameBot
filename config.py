from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

BOT_TOKEN = getenv("BOT_TOKEN", "6648598150:AAFGZvnVU1pOQlmDDQ-OHUI_KI2NCi0cmBM")
BOT_NAME = getenv("BOT_NAME", "GameYoxlamaBot") 
API_ID = int(getenv("API_ID" 29171757))
API_HASH = getenv("API_HASH", ""f2a2d9619b545d116fc42b5fee5d592e")
BOT_USERNAME = getenv("BOT_USERNAME", "GameYoxlamaBot")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Kolgeli:sesiz@cluster0.sgubr8z.mongodb.net/Elmdar?retryWrites=true&w=majority")
