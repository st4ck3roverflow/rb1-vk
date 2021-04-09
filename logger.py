import logging

logger = logging.getLogger("RBC")
logger.setLevel(logging.INFO)
fh = logging.FileHandler("rbc.log")
formatter = logging.Formatter('[%(asctime)s] [%(name)s/%(levelname)s]: %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


def log_info(message):
    logger.info(message)
    print("[INFO] " + str(message))


def log_warn(message):
    logger.warning(message)
    print("[WARN] " + str(message))


def log_error(message):
    logger.error(message)
    print("[ERROR] " + str(message))
    log_info("Stopping our process")
