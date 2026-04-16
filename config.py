import os
from dotenv import load_dotenv

load_dotenv()

AFRI_API_KEY = os.getenv("AFRI_API_KEY")
AFRI_BASE_URL = os.getenv("AFRI_BASE_URL", "https://build.lewisnote.com/v1")

# Modèles disponibles
MODELS = {
    "rapide": "gpt-5.4-nano",
    "standard": "gpt-5.4-mini",
    "puissant": "gpt-5.4",
    "pro": "gpt-5.4-pro",
    "code": "gpt-5.3-codex"
}