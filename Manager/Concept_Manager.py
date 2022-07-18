#管理所有Concept
from Support.Checking_Process import Check_Code
from Support.Exception import CheckCodeError
import logging
import inspect
import re

class Concept_Manager:
    def __init__(self,check_code : str):
        self.logger=logging.getLogger("MainLogger")
        judge,module_list=Check_Code(check_code,"Concept")
        if judge==False:
            raise CheckCodeError(check_code)
        else:
            for module in module_list:
                self.Concept_Importer(module)
        self.Show_Concept_Types()
        self.a=BasicConcept(1,2)

    def Concept_Importer(self,num):
        '''
        概念导入器
        :param num: 导入码
        :return: True
        '''
        if num == '1':
            global BasicConcept,Point,Line,Oval
            from Library.concept.MetaConcept import BasicConcept,Point,Line,Oval
            self.logger.info("成功导入Concept模块MetaConcept:BasicConcept,Point,Line,Oval")
        return True

    def Show_Concept_Types(self):
        self.concept_types=[]
        for item in globals().items():
            if inspect.isclass(item[1])==True:
                if 'Library' in str(item[1]):
                    self.concept_types.append(re.findall('\.(\w+)\'',str(item[1]))[0])
        self.logger.info("已导入的模块:{}".format(str(self.concept_types).replace("[","").replace("]","")))