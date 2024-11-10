# src/logger.py
"""
日志记录模块，配置并提供日志记录功能。
"""

import logging
import os
from logging.handlers import RotatingFileHandler

# 定义日志记录器的名称
LOGGER_NAME = 'SyncMasterLogger'

# 创建日志记录器
logger = logging.getLogger(LOGGER_NAME)
logger.setLevel(logging.DEBUG)  # 设置最低日志级别为DEBUG

# 确保日志目录存在
LOG_DIR = 'logs'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# 定义日志文件路径
LOG_FILE = os.path.join(LOG_DIR, 'syncmaster.log')

# 创建旋转文件处理器，限制单个日志文件大小为5MB，最多保留5个备份
file_handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=5)
file_handler.setLevel(logging.DEBUG)  # 设置文件处理器的日志级别

# 创建控制台处理器，输出INFO级别及以上的日志到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 定义日志格式
formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 避免重复添加处理器
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# 禁止传播到父日志记录器
logger.propagate = False
