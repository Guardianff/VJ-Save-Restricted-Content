import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7334566762:AAFTDty0k5zUhKqmy5H24LurCtGqF-OXbK4")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27485646"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "60d9b4cac575e735e25c1a00885e91d9")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6073523936"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://AMMAAAAA:AMMAAAAA@cluster0.eulppgg.mongodb.net/?retryWrites=true&w=majority") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
