# 机器学习任务-分类
  
  这一类分类任务中,其输出值是整数,整数标志的是目标的种类.本章提供了一个分类问题常用的程序模版.  常见的分类算法有以下几种:
    

*  [Logistic Regression](https://github.com/hanxinle/practical_machine_learning/tree/master/3_Classification/Logistic_Regression)

    不少人把Logistic Regression称为“逻辑回归”，但实际上logistic和中文“逻辑”(logic) 没半毛钱关系。LR是广义线性模型，把线性回归y=w^T x的y换成ln[p/(1-p)]即得，p是p(y=1|x)。p/(1-p)是“几率”，所以LR应称为“对数几率回归”.(引自微博:南大周志华)

    在<机器学习实战>中已经有所提及,引入该方法的目的是借用S函数的"阶跃"的性质,实际上,在本节所给的示例中,根据年龄\年收入判断用户是否会对某品牌汽车有购买倾向也是利用了这一性质,超过50%即认为用户有购买倾向,反之则没有,而不能理解为该方法二分类的常用手段.
    
    
