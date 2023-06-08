import logging
from config import LOGGER_LEVEL


main_logger = logging.getLogger('logger')
main_logger.setLevel(LOGGER_LEVEL)

handler = logging.FileHandler(f"logger.log", mode='w')
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

handler.setFormatter(formatter)
main_logger.addHandler(handler)

class logger:
    def debug(msg: str):
        main_logger.debug(msg)
    def info(msg: str):
        main_logger.info(msg)
    def warning(msg: str):
        main_logger.warning(msg)
    def error(msg: str):
        main_logger.error(msg)
    def critical(msg: str):
        main_logger.critical(msg)
