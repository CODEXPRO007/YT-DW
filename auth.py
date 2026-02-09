API_KEYS = {
    "FREE123": "free",
    "PREMIUM999": "premium"
}

def check_key(key):
    return API_KEYS.get(key)