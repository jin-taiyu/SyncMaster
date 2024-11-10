### SyncMaster

[![Python application](https://github.com/jin-taiyu/SyncMaster/actions/workflows/python-app.yml/badge.svg)](https://github.com/jin-taiyu/SyncMaster/actions/workflows/python-app.yml)

SyncMaster 是一个跨平台的文件同步工具，设计用于在本地存储与长期连接的外置存储系统之间实现高效、可靠的文件同步。项目专为多路径文件/文件夹对的同步需求而设计，支持检测并处理文件的增、删、改操作，确保两端数据的一致性，项目目前仍在开发阶段。

#### 项目目录结构

```plaintext
SyncMaster/
├── README.md               
├── requirements.txt        
├── .gitignore              
├── setup.py                # 项目的安装和部署配置
├── src/                    # 存放源代码的目录
│   ├── __init__.py         
│   ├── main.py             # 程序的入口文件
│   ├── ui.py               # 用户界面模块
│   ├── file_scan.py        # 文件扫描和比较模块
│   ├── sync_logic.py       # 同步逻辑模块
│   ├── file_ops.py         # 文件操作模块
│   ├── config_manager.py   # 配置管理模块
│   ├── logger.py           # 日志记录模块
│   └── exceptions.py       # 自定义异常模块
├── tests/                  # 存放测试代码的目录
│   ├── __init__.py         
│   ├── test_file_scan.py   # 针对file_scan.py的测试。
│   ├── test_sync_logic.py  # 针对sync_logic.py的测试。
│   ├── test_file_ops.py    # 针对file_ops.py的测试。
│   ├── test_config_manager.py # 针对config_manager.py的测试。
│   └── test_logger.py      # 针对logger.py的测试。

```
