
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "1c9cbb3c-9790-4f7a-8b1d-68c38e9d44308e6d4c7a-d126-4a7e-9f0a-91fd1cc0fb1a6c58e162-abae-4a84-a2d3-7996086ff020"
NEVERCACHE_KEY = "b61bd287-d328-475a-a9fd-7ea05dc5f84321d1ec45-9777-43e4-a78c-7cd6b64dcab6eece9f2a-1098-42bd-8b03-525d93d82a71"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
