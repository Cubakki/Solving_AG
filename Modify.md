# 相较于原系统的主要修改部分

#### *将Operator合并于Rule中

对元素进行操作时，之前的做法是先搜索规则，再套用规则应用Operator，这两步是可以合并的，即在规则中直接定义Operator；关于Operator在Term中的应用见下条

进一步地，部分Operator(如XCoordinate(P))可以转化为实例的属性，另一部分Operator(如Distance(A,B))可以转化为Rule

### *删去了Term和Individual

Term是一个【Operator作用于一些元素上（的返回值）】的实例，譬如两点间的距离我们用Term【Lenth(A,B)】表示。但是，这样无疑是功能重复的，我们完全可以定义一个Concept类，将Operator的功能移植于__init__过程中，用其实例替代Term；类似地，Individual可以使用Concept的实例和定义运算规则替代

### *添加了Undetermined类

有一个未知数管理器统一管理现存的所有未知数，Undetermined类继承了Symbol并添加了一些独特的标记

### *（待定）对于Concept的修改

一种想法是将诸如XCoordinate(P)的Term归化为Concept的私有属性

另一种想法是将一些Operator（X）形式的元素移植为特殊的Concept类或一种新的类型

比较好的情况是整个解题过程中只存在Concept实例和Rule，且一部分的Rule可以在Concept实例初始化时执行

可以考虑Rule只保留Concept实例间互相作用的部分，其它Rule作为Concept的内部函数或自动执行的函数。需要评估选取耗时和执行耗时做出判断

由于整个系统时模块化的，以上设想可以同时实现（由Concept管理器管理，不同策略由校验码匹配）

## ***我们不关注获取某一信息具体需要用到某个函数（按之前的方法，即哪个Operator），而是关注每一种信息有至少一个Rule提供获取它的方法（途径）。我们将对Rule进行校验以确认系统的完整性。必要时，可以对Concept的方法进行修改以适应Rule的需要。形象地说，Rule是提出需求地一方，整个数据结构是以实现Rule的完整性为中心的。
