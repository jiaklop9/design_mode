# design_mode
Python设计模式
### 什么是设计模式
&ensp;设计模式是前辈们对开发经验的总结，是解决特定问题的一系列套路，它不是语法规定，而是一套用来提高代码可复用性、可维护性、可读性、稳健性以及安全性的解决方案。
### 设计模式分类
三类：<br>
1)创建型模式：
    单例、工厂、抽象工厂、建造者、原型<br>
2)结构型型模式：
    适配器、桥接、装饰器、组合、外观、享元、代理<br>
3)行为型模式：
    模板方法、命令、迭代器、观察者、中介、备忘录、解释器、状态、策略、职责链、访问者<br>
### 设计模式意义
设计模式的本质是面向对象设计原则的实际运用，是对类的继承封装性、继承性、和多态性以及类的关联关系和组合关系的充分理解。

### 设计模式目的
编写软件过程中，程序员面临着来自耦合性，内聚性，以及可维护性，可扩展性，重要性，灵活性等多方面挑战，设计模式是为了让程序具有更好的:<br>
    1) 代码重用性（即：相同的功能代码。不用多次编写）<br>
    2）可读性（即：编程规范性，便于其他程序员阅读与理解）<br>
    3）可扩展性（即： 当需要新增功能时，非常方便，称为可维护性）<br>
    4）可靠性（即：当我们新增功能后，对原来的功能没有影响）<br>
    5）使程序呈现高内聚，低=耦合的特性。<br>

### 设计模式七大原则
1）单一职责：
    控制类的粒度大小，将对象解耦，提高内聚性<br>
2）接口隔离：
    要为各个类建立它们需要的专用接口<br>
3）依赖倒转：
    面向接口编程，不要面向实现编程<br>
4）里氏替换原则：
    继承必须确保超类所拥有的性值在子类中仍然成立<br>
5）开闭原则：
    对外扩展开放，对修改关闭<br>
6）迪米特法则：
    只与你的直接朋友交谈，不跟 "陌生人" 说话<br>
7）合成复用：
    尽量先使用组合或者聚合等关联关系来实现，其次才考虑使用继承关系来实现<br>