from typing import Union,List
import logging
Accepted_Code=["1#1#1"]
logger=logging.getLogger("MainLogger")
#---------------------------------------------------- 校验码对应关系
'''
校验码接受str格式,校验码用于检验并导入对应的模块组
由于Concept、Rule乃至于搜索算法都是模块化的，我们需要一种机制来判断某种模块组合是可行的，并将它们导入对应的管理器中。
校验码就承担了这一功能。校验码中的#隔开不同类的模块，-隔开同类模块中的不同模块，顺序与对应关系见下表:

第一位-Concept:
1--------------MetaConcept

第二位-Rule:
1--------------

第三位-Search(Eingine):
1--------------

'''
def Check_Code(Check_Code : Union[int,str],Module : str):
    '''
    验证校验码，若成功则将校验码分割为一个嵌套列表传递给Apply_Code
    :param Check_Code: 校验码，规则见./Support/Checking_Process
    :param Module: 字符串，"Concept"/"Rule"/"Search"
    :return: True/Flase
    '''
    if Check_Code in Accepted_Code:
        Concept_Code = (Check_Code.split("#")[0]).split("-")
        Rule_Code    = (Check_Code.split("#")[1]).split("-")
        Search_Code  = (Check_Code.split("#")[2]).split("-")
        logger.info("校验码校验成功")
        if Module=="Concept":
            return [True,Concept_Code]
        elif Module=="Rule":
            return [True,Rule_Code]
        elif Module=="Search":
            return [True,Search_Code]
    else:
        return [False,False]

# def Apply_Code(Code : List,Module : str):  #由于导入相关问题，移至对应管理器中；后期考虑注册形式
#     '''
#     导入对应模块
#     :param Code: 嵌套列表,[[Concept_Code_List],[Rule_Code_List],[Search_Code_List]]
#     :param Module: 字符串，"Concept"/"Rule"/"Search"
#     :return: True
#     '''
#     Module2Position={"Concept":0,"Rule":1,"Search":2}
#     Trans_Module=Module2Position[Module]
#     if Trans_Module==0:
#         for num in Code:
#             Concept_Importer(num)
#     elif Trans_Module==1:
#         for num in Code:
#             Rule_Importer(num)
#     elif Trans_Module==2:
#         for num in Code:
#             Search_Importer(num)
#     return True
#
# def Concept_Importer(num):
#     '''
#     概念导入器
#     :param num: 导入码
#     :return: True
#     '''
#     if num=='1':
#         global BasicConcept,Point,Line,Oval
#         from Library.concept.MetaConcept import BasicConcept,Point,Line,Oval
#         logger.info("成功导入Concept模块MetaConcept:BasicConcept,Point,Line,Oval")
#     return True
#
# def Rule_Importer(num):
#     '''
#     规则导入器
#     :param num: 导入码
#     :return: True
#     '''
#     if num=='1':
#         pass
#     return True
#
# def Search_Importer(num):
#     '''
#     搜索算法导入器
#     :param num: 导入码
#     :return: True
#     '''
#     if num=='1':
#         pass
#     return True