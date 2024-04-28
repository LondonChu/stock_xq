import logging, os
from datetime import datetime


dir_path = "./Logs/"  # 設定 logs 根目錄
filename = "{:%Y-%m-%d}".format(datetime.now()) + ".log"  # 設定檔名

def create_logger():
    # config
    logging.captureWarnings(True)  # 捕捉 python waring message
    formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(message)s")
    my_logger = logging.getLogger("py.warnings")
    my_logger.setLevel(logging.INFO)

    # 若不存在目錄則新建
    if (not os.path.exists(dir_path)):
        os.makedirs(dir_path)

    # file handler
    fileHandler = logging.FileHandler(dir_path + '/' + filename, 'a', 'utf-8')
    fileHandler.setFormatter(formatter)
    my_logger.addHandler(fileHandler)

    # console handler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
    consoleHandler.setFormatter(formatter)
    my_logger.addHandler(consoleHandler)

    return my_logger

