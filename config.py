from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

BOT_TOKEN = getenv("BOT_TOKEN", "5537646590:AAEwqO5MazvP_Kfmaf-bLdunbslxpO8s7KY")
BOT_NAME = getenv("BOT_NAME", "CrocadilBot") 
API_ID = int(getenv("API_ID" 13544181))
API_HASH = getenv("API_HASH", "1cf5e591506286e82e89e98b2436ebb6")
BOT_USERNAME = getenv("BOT_USERNAME", "Corcadildsidhlebot")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://kenanbitcoin:PunnUo7gN6XpNidk@cluster0.gtmaj.mongodb.net/Cluster0?retryWrites=true&w=majority")
