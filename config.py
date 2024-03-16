# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "24482734")

API_HASH = os.environ.get("API_HASH", "5ccf6a58166cc047a7eba01c5dbc930c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6983906880:AAHQ-cMBi0fAVPyJSJ_1NNFM2nDGgA84AZM") 

FORCE_SUB = os.environ.get("FORCE_SUB", "TN69Links") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "tn69links")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://tn69links:cY6oAdj4gRdX2ytN@cluster0.sga3dau.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/116c855721726d2a8a250.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1790775725').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
