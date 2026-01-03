#Supoort group @rexbotschat
#Supoort group @rexbotschat
#Supoort group @rexbotschat
# Rexbots
# Don't Remove Credit
# Telegram Channel @RexBots_Official 
#Supoort group @rexbotschat


import os

class Config:
    BOT_TOKEN = "8314065055:AAGjTymsm-p8dK4432AEltF4IA751jgwly0"
    USER_ID = 8226767954
    API_ID = 23537462
    API_HASH = "c9599a5aa61ee8ca4f5e778d20c61f24"
    DB_NAME = "cluster0"
    DB_URL = "mongodb+srv://autorename:fbMbsVFICHccoTup@cluster0.uygy8qe.mongodb.net/"
    CHECK_INTERVAL = 300
    MAX_CHAPTERS_PER_CHECK = int(os.getenv("MAX_CHAPTERS", "5"))
    DOWNLOAD_DIR = "downloads"
    STATE_FILE = "bot_state.json"
    CACHE_FILE = "manga_ids_cache.json"
    API_BASE = "https://api.mangadex.org"
    WEB_BASE = "https://mangadex.org"
    LOOKBACK_HOURS = 24
    MAX_IMAGE_SIZE = 10 * 1024 * 1024
    MAX_PDF_SIZE = 50 * 1024 * 1024
    USE_DATABASE = os.getenv("USE_DATABASE", "True").lower() == "True"
    
    PORT = int(os.getenv("PORT", "8080"))
    TG_BOT_WORKERS = int(os.getenv("TG_BOT_WORKERS", "4"))

    PICS = [
        "https://ibb.co/VYSPzSDH","https://ibb.co/rGTqCwBV","https://ibb.co/r2QZ0T0q","https://ibb.co/67kGFzC5","https://ibb.co/gZh6qysN","https://ibb.co/0ysjvb0t","https://ibb.co/7dGbyPvk"
    ]

    DEFAULT_FILENAME_FORMAT = "{manga_name} [Ch-{chapter}]"


# Rexbots
# Don't Remove Credit
# Telegram Channel @RexBots_Official 
#Supoort group @rexbotschat
