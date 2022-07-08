# 开发文档

## 日志模块

路径  ./Log

.Log/Logging_File 日志文件路径

Log.py            用于logger与handler的初始化，在Main中被调用

log_set.ymal      日志配置文件，在Log.log_init()中被使用

基于全局包logging，构造了MainLogger和root两个logger，主要使用前者，包含了一个控制台handler和两个filehandler，日志文件记录于./Log/Logging_File

调用此模块可直接import logging，并利用logger=logging.getLogger("Mainlogger")获取记录器
