import copy
from Support.Exception import SelfKeyError
from Library.undetermined import Undetermined
from typing import Union,Optional,List
#MetaConcept包含了最基础的二维概念
#本版本中，准线、焦点等概念作为其母体的属性表示，而非单独成为一个Concept，这样做是为了减少搜索时的实例规模

'''
概念的基类
'''
class BasicConcept:
    undetermined_flag         : bool # 未知数标记
    undetermined_num          : int  # 未知数数目
    undetermined_dict         : dict # 未知数键值对字典
    undetermined_dict_origin  : dict # 初始化时的未知数键值对（记录用）

    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.undetermined_flag = False
        self.undetermined_num = 0
        self.undetermined_dict = {}
        self.fresh_undetermined_inf(init=True)
        pass

    def fresh_undetermined_inf(self,init=False):  #更新类内未知数相关属性的方法
        self.undetermined_num=0
        self.undetermined_dict={}
        for obj in self.__dict__.items():
            if type(obj[1])==Undetermined:
                self.undetermined_dict[obj[0]]=obj[1]
                self.undetermined_num+=1
        if self.undetermined_num==0:
            self.undetermined_flag=True
        if init == True:
            self.undetermined_dict_origin=self.undetermined_dict
        # print(self.undetermined_dict)
        return (self.undetermined_flag,self.undetermined_num,self.undetermined_dict)

    def check_undetermined_status(self): #检查并更新类内未知数状态，若已解出则更新为确切值,返回的布尔值表示是否有变更
        modified : bool =False
        for undetermineds in self.undetermined_dict.items():
            if undetermineds[1].solved == True:
                modified=True
                self.__dict__[undetermineds[0]]=undetermineds[1].value
        self.fresh_undetermined_inf()
        return modified

    def update(self,undetermind,solved_value):
        for obj in self.__dict__.items():
            if obj[1]==undetermind:
                self.__dict__[obj[0]]=solved_value

    def get(self,*keys):
        output=[]
        try:
            for key in keys:
                if key in self.__dict__.keys():
                    output.append(self.__dict__[key])
                else:
                    raise SelfKeyError(self.name,keys)
        except SelfKeyError as e:
            pass

    def self_hook(self,func):       #回调函数接口
        func(self)


#-----------------------------------------------------------------------------------------------------------------
class Point(BasicConcept):
    AxisX  : Union[int,float,Undetermined]   #x坐标
    AxisY  : Union[int,float,Undetermined]   #y坐标

    def __init__(self,id,name,AxisX,AxisY):  #AxisX和AxisY未定时，由注册器向待定系数管理器申请新的待定系数并填入
        self.AxisX=AxisX
        self.AxisY=AxisY
        self.undetermined_flag=False
        self.undetermined_num=0
        self.undetermined_dict={}
        BasicConcept.__init__(self, id, name)


#-----------------------------------------------------------------------------------------------------------------
class Line(BasicConcept):
    #采用一般方程Ax+By=C=0，K由一个关系式给出，每次
    ParaA : Union[int,float,Undetermined]
    ParaB : Union[int,float,Undetermined]
    ParaC : Union[int,float,Undetermined]
    Slope : Union[int,float,Undetermined,None] #None时表示斜率不存在
    restricted : Optional[dict] #None时表示约束不存在，即为直线
    #不为None时，格式为{“x”:[[">",value],[",",value]],“y”:[[">",value],[",",value]]}
    #初始化时可以以双端点的形式输入，[Point,Point],其中左右端点严格按照次序排列，否则默认为标准格式
    Known_point : Optional[List[Point]]

    def __init__(self,id,name,x,y,ParaA=None,ParaB=None,ParaC=None,restricted : Optional[dict]=None):
        BasicConcept.__init__(self,id,name)
        self.ParaA=ParaA
        self.ParaB=ParaB
        self.ParaC=ParaC
        self.Slope=(self.ParaA/self.ParaB)
        self.Points={}
        self.Equation=self.ParaA*x+self.ParaB*y+self.ParaC
        self.restricted_init(restricted)

    def point_register(self,claim : str,point :Point):
        #claim作为点的声明，一般点动态生成，特殊点（如与坐标轴交点等）有确定的声明方式
        #点注册器,目前考虑将代入点解方程操作置于外部藉由Rule实现
        #可以考虑将直线与坐标轴的交点作为特殊点，在初始化中添加
        self.Points[claim]=point
        return True

    def get_slope(self):  #由于Slope是ParaA和ParaB的函数，本身就是动态的；这里定义一个手动获取
        tip=False  #是否含未知数标记
        if (type(self.ParaA)==Undetermined or type(self.ParaB)==Undetermined):
            tip=True
        self.Slope=self.ParaA/self.ParaB
        return (tip,self.Slope)

    def restricted_init(self,restricted):
        if type(restricted)!=list:
            self.restricted=restricted
        else:
            self.restricted={"x":[[">",restricted[0].AxisX],["<",restricted[1].AxisX]],
                             "y":[[">",restricted[0].AxisY],["<",restricted[1].AxisY]]}
        return True

#-----------------------------------------------------------------------------------------------------------------
'''
由于诸如离心率、参量C等参数都是动态定义的，因此直接对实例提取对应的属性应该是正确的；为了方便考虑，对它们亦会添加对应的提取函数
需要考虑的是，哪一部分属性需要在规则的作用函数中定义，哪一部分属性应该直接在Concept中定义，譬如离心率定义为ParaC/ParaA,它显然可以在Concept
中动态定义，将这个过程移至规则中是冗余的，可以将规则的作用函数定义为获取Oval.Eccentricity
'''
class Oval(BasicConcept):
    #形式为x^2/a^2+y^2/b^2=1
    ParaA : Union[int,float,Undetermined]
    ParaB : Union[int,float,Undetermined]
    ParaC : Union[int,float,Undetermined]
    Eccentricity : Union[int,float,Undetermined]   #离心率

    def __init__(self,id,name,x,y,ParaA=None,ParaB=None):
        BasicConcept.__init__(self,id,name)
        self.ParaA=ParaA
        self.ParaB=ParaB
        self.ParaC=pow(((self.ParaA)**2-(self.ParaB)**2),0.5)
        self.Eccentricity=self.ParaC/self.ParaA
        self.x=x
        self.y=y