# 开发文档

## 日志（Log）

路径  ./Log

### **### ./Log/Logging_File 日志文件路径**

**Log.py            用于logger与handler的初始化，在Main中被调用**

基于全局包logging，构造了MainLogger和root两个logger，主要使用前者，包含了一个控制台handler和两个filehandler，日志文件记录于./Log/Logging_File

调用此模块可直接import logging，并利用logger=logging.getLogger("Mainlogger")获取记录器

**log_set.ymal      日志配置文件，在Log.log_init()中被使用**

## 库（Library）

路径 ./Library

存储必要的数据，如Concept、Rule等

### ./Library/concept concept数据库目录

**MetaConcept.py   存储基本的二维概念，包括基类、点类、线类、圆锥曲线类等**

实现了BaseConcept、Point、Line、Oval类

### ./Library/undetermined  undetermined类型目录

**undetermined.py  存储undetermined类，继承并覆写sympy中的Symbol类，添加了若干属性和方法**

### ./Library/rule  Rule数据库目录

## 管理器(Manager)

路径 ./Manager

管理不同的资源和模块

**Concept_Manager.py  概念类型管理器，维护一张可用概念表，提供一个动态生成概念实例的接口**

## 辅助模块(Support)

路径 .\Support

**Exception.py  定义一系列异常，被raise时将标准化的消息输出至日志。这一系列异常都将在主循环或调度器中被捕获并处理**

**Checking_Process.py 提供校验码的验证和拆解解决方案，保证只有特定的模块组合（可以工作的）才会被接受并加载**
