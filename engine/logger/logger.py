import datetime
import logging
from pathlib import Path

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def create_logger(logger_name: str, file_debug_level: int, console_debug_level: int, logs_directory: Path):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    fh = logging.FileHandler(Path(LOGS_DIR, datetime.date.today().strftime("%B %d, %Y") + ".log"))
    fh.setLevel(file_debug_level)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(console_debug_level)
    # create formatter and add it to the handlers
    formatter = logging.Formatter(FORMAT)
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


LOGS_DIR = "logs/"


class EngineLogger:
    logger = create_logger(logger_name="engine_logger",
                           file_debug_level=logging.INFO,
                           console_debug_level=logging.DEBUG,
                           logs_directory=Path("logs"))

    @staticmethod
    def debug(text: str) -> None:
        EngineLogger.logger.debug(text)

    @staticmethod
    def warn(text: str) -> None:
        EngineLogger.logger.warning(text)

    @staticmethod
    def info(text: str) -> None:
        EngineLogger.logger.info(text)

    @staticmethod
    def error(text: str) -> None:
        EngineLogger.logger.error(text)

    @staticmethod
    def critical(text: str) -> None:
        EngineLogger.logger.critical(text)
