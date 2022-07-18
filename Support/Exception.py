import logging
from typing import Union,Tuple,List
#添加异常类型
#抛出的异常会同步到日志和控制台中
logger=logging.getLogger("MainLogger")

class SelfKeyError(BaseException):
    def __init__(self,name,keys : Union[List,Tuple]):
        self.keys=list(keys)
        self.name=name
        self.msg="SelfKeyError:对{}获取属性时，提供的key:{}不正确".format(self.name,[x for x in self.keys])
        self.SelfKeyError_Handler()

    def SelfKeyError_Handler(self):
        logger.error(self.msg)

class CheckCodeError(BaseException):
    def __init__(self,Checked_Code):
        self.Checked_Code=Checked_Code
        self.CheckCodeError_Handler()

    def CheckCodeError_Handler(self):
        logger.error("校验码{}未被接受，退回至主循环".format(self.Checked_Code))