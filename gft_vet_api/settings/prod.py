from .base import *
from decouple import config
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': dj_database_url.config(default=config("DATABASE_URL"))
}
