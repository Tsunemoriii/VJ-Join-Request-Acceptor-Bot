from os import environ

API_ID = int(environ.get("API_ID", "20628383"))
API_HASH = environ.get("API_HASH", "65a242463b8af9ba7b3c41d8de9738d1")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001537276104"))
ADMINS = int(environ.get("ADMINS", "1921693263"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://utahheroku12:utahheroku12@cluster0.igy9p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
