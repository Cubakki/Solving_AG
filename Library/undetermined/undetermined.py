#定义了未知数(undetermined)类
from sympy import Symbol


'''
Symbol类的赋值(字母)在__new_stage2__中完成，因此对Undetermined类初始化提供的name会首先作为Symbol的字母符号使用
因此对Undetermined的创建过程与Symbol一致:
    a=Undetermined("a")
'''
class Undetermined(Symbol):
    def __init__(self,name : str,locked : bool = False): #locked置为True代表此未知数不可修改(如x、y)
        Symbol.__init__(self)
        self.name=name
        self.solved = False
        self.value  = None
        self.locked = locked

    def update(self,value):#传入并更新未知数状态和确切值
        if self.locked == True:
            return False
        self.value=value
        if type(value)!=Undetermined:
            self.solved=True

#未知数管理器会预留x、y两个Undetermined实例
