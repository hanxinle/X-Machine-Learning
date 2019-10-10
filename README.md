# 机器学习实战

我将机器学习方法分为三类,回归\分类\聚类,这三类算法涵盖了大多数的机器学习算法,回归的结果是实数(整数+小数),分类的结果可以视作整数(label),聚类是对数据的 整理.

[0 环境配置(Python版)](https://github.com/hanxinle/practical_machine_learning/tree/master/0_get_start)

[1 数据的预处理](https://github.com/hanxinle/practical_machine_learning/tree/master/1_data_processing)

[2 回归](https://github.com/hanxinle/practical_machine_learning/tree/master/2_Regressing)

* [简单线性回归](https://github.com/hanxinle/practical_machine_learning/tree/master/2_Regressing/Simple%20Linear%20Regression)

  这个模型建立了工作经验与工资之间的关系,可以根据工作年限预测工资水平.

* [多元线性回归](https://github.com/hanxinle/practical_machine_learning/tree/master/2_Regressing/Multiple%20Linear%20Regression)

  这个模型针对50家公司运营的数据建立多元线性模型,自变量是研发费用,广告费用,市场推广费用,公司地点,因变量是营业额.这个示例中,在建立模型前,需要对自变量工作地点进行虚拟编码,并且舍弃一项(原因见notebook文件),对生成的初始模型进行进行优化,本示例采用反向删除的方法,去除对模型影响较小的因变量模型,获得更加简洁,更具鲁棒性的模型.
