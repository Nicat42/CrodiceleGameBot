from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

BOT_TOKEN = getenv("BOT_TOKEN", "5631477617:AAFrf8wg07Anl5MpmZj3LMPCEZkJw966hCM")
BOT_NAME = getenv("BOT_NAME", "Wieuehebot") 
API_ID = int(getenv("API_ID" 13544181))
API_HASH = getenv("API_HASH", "1cf5e591506286e82e89e98b2436ebb6")
BOT_USERNAME = getenv("BOT_USERNAME", "Wieuehebot")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Kolgeli:sesiz@cluster0.sgubr8z.mongodb.net/Elmdar?retryWrites=true&w=majority")
