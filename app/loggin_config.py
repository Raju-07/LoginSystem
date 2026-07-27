import logging
import logging.config
from pathlib import Path
from typing import Any,Dict
from app.core.config import settings

#Defining Log directories

LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"
AUTH_FILE = LOG_DIR / "auth.log"
DB_FILE = LOG_DIR / 'db.log'
REDIS_FILE = LOG_DIR / 'redis.log'
SERVER_FILE = LOG_DIR / 'server.log'


# Setting logs config

def setup_logging(debug:bool = settings.debug):
    '''
    Configure logging with conditional output.
    Args:
        debug: if true, logs in the console else in the file
    '''

    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    logging_config: Dict[str,Any] = {
        "version":1,
        "disable_existing_loggers":False,
        "formatters":{
            "standard":{
                "format":log_format,
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        "handlers":{
            "console":{
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "standard",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter":"standard",
                "filename": str(LOG_FILE),
                "maxBytes": 10485760, #10 MB
                "backupCount":5,
            },
            "auth_file":{
               "class" : "logging.RotatingFileHandler",
               "level" : "INFO",
               "formatter": "standard",
               "filename" : str(AUTH_FILE),
               "maxBytes" : 10485760, #10 MB
               "backupCount" : 5,
            },
            "db_file" : {
                "class" : "logging.RotatingFileHandler",
                "level" : "INFO",
                "formatter" : "standard",
                "filename" : str(DB_FILE),
                "maxBytes" : 10485760, # 10 MB
                "backupCount" : 5,
            },
            "redis_file" : {
                "class" : "logging.RotatingFileHandler",
                "level" : "INFO",
                "formatter" : "standard",
                "filename" : str(REDIS_FILE),
                "maxBytes" : 10485760, # 10 MB
                "backupCount" : 5,
            },
            "server_file" : {
                "class" : "logging.RotatingFileHandler",
                "level" : "INFO",
                "formatter" : "standard",
                "filename" : str(SERVER_FILE),
                "maxBytes" : 10485760, # 10 MB
                "backupCount" : 5,
            },
        },
        "loggers" : {
            "uvicorn": {
            "handlers" : ["console" if debug else "server_file"],
            "level" : "DEBUG" if debug else "INFO",
            "propagate" : False,
            },
            "app" : {
                "handlers" : ['console' if debug else 'file'],
                'level' : 'DEBUG' if debug else 'INFO',
                'propagate' : False,
            },
            "app.auth" : {
                'handlers': ['console' if debug else 'auth_file'],
                'level' : 'DEBUG' if debug else 'INFO',
                'propagate' : False,
            },
            'app.db' : {
                'handlers' : ['console' if debug else 'db_file'],
                'level' : 'DEBUG' if debug else "INFO",
                'propagate' : False,
            },
            'app.redis' : {
                'handlers' : ['console' if debug else 'redis_file'],
                'level' : 'DEBUG' if debug else 'INFO',
                'propagate' : False,
            },
            'watchfiles': {
                'level' : "WARNING",
                'propagate' : False,
            },
        },
        'root' : {
            'handlers' : ['console' if debug else 'file'],
            'level' : "DEBUG" if debug else "INFO",
        }
    }

    logging.config.dictConfig(logging_config)