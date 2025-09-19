import os

# Создаем директорию для логов
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "utils_handler": {
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "utils.log"),
            "encoding": "utf-8",
            "formatter": "standard",
            "level": "DEBUG",
            "mode": "w",
        },
        "external_api_handler": {
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "external_api.log"),
            "encoding": "utf-8",
            "formatter": "standard",
            "level": "DEBUG",
            "mode": "w",
        },
        "main_handler": {
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "main.log"),
            "encoding": "utf-8",
            "formatter": "standard",
            "level": "DEBUG",
            "mode": "w",
        },
        "masks_handler": {
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "masks.log"),
            "encoding": "utf-8",
            "formatter": "standard",
            "level": "DEBUG",
            "mode": "w",
        },
        "common_handler": {
            "class": "logging.FileHandler",
            "filename": os.path.join(LOGS_DIR, "full.log"),
            "encoding": "utf-8",
            "formatter": "standard",
            "level": "DEBUG",
            "mode": "w",
        },
    },
    "loggers": {
        "utils": {
            "handlers": ["utils_handler", "common_handler"],
            "level": "DEBUG",
            "propagate": False,
        },
        "external_api": {
            "handlers": ["external_api_handler", "common_handler"],
            "level": "DEBUG",
            "propagate": False,
        },
        "masks": {
            "handlers": ["masks_handler", "common_handler"],
            "level": "DEBUG",
            "propagate": False,
        },
        "main": {
            "handlers": ["main_handler", "common_handler"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
