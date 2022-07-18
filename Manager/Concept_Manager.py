#管理所有Concept
from Support.Checking_Process import Check_Code,Apply_Code
from Support.Exception import CheckCodeError
import logging
import inspect

class Concept_Manager:
    def __init__(self,check_code : str):
        self.logger=logging.getLogger("MainLogger")
        judge,module_list=Check_Code(check_code,"Concept")
        if judge==False:
            raise CheckCodeError(check_code)
        else:
            for module in module_list:
                self.Concept_Importer(module)
        self.show_concept_types()
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

    def show_concept_types(self):
        for item in globals().items():
            if inspect.isclass(item[1])==True:
                print(item[1])