import logging


class Logger:
    def __init__(self, logger_name) -> None:
        super().__init__()
        
        self.logger = logging.Logger(logger_name)
        self.logger.setLevel(0)

        handler = logging.FileHandler("wins_log.log", mode='w')
        formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)
