import logging


class loggers():
    def __init__(self, log_name: str):
        super().__init__()
        
        # настройки логера
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(10)

        handler = logging.FileHandler(f"wins_log.log", mode='w')
        formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        handler.setFormatter(formatter)
        
        self.logger.addHandler(handler)
