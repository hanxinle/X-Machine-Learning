# 机器学习的应用

我将机器学习方法分为三类,回归\分类\聚类,这三类算法涵盖了大多数的机器学习算法,回归的结果是实数(整数+小数),分类的结果可以视作整数(label),聚类是对数据的 整理.

[0 环境配置(Python版)](https://github.com/hanxinle/practical_machine_learning/tree/master/0_get_start)

[1 数据的预处理](https://github.com/hanxinle/practical_machine_learning/tree/master/1_data_processing)

[2 回归](https://github.com/hanxinle/practical_machine_learning/tree/master/2_Regression)

* [简单线性回归](https://github.com/hanxinle/practical_machine_learning/tree/master/2_Regression/Simple%20Linear%20Regression)

  这个模型建立了工作经验与工资之间的关系,可以根据工作年限预测工资水平.

* [多元线性回归](https://github.com/hanxinle/practical_machine_learning/tree/master/2_Regression/Multiple%20Linear%20Regression)

  这个模型针对50家公司运营的数据建立多元线性模型,自变量是研发费用,广告费用,市场推广费用,公司地点,因变量是营业额.这个示例中,在建立模型前,需要对自变量工作地点进行虚拟编码,并且舍弃一项(原因见notebook文件),对生成的初始模型进行进行优化,本示例采用反向删除的方法,去除对模型影响较小的因变量模型,获得更加简洁,更具鲁棒性的模型.

* [多项式回归](https://github.com/hanxinle/practical_machine_learning/tree/master/2_Regression/Polynomial%20Regression)

  它的内涵是因变量能用系数的线性关系表示,不是用自变量的线性来表征.它与多元线性回归有很多相似处,它是简单线性回归的延伸,本身不是线性模型.这一方法适合自变量较少的情形.

  这个模型预测新人在原公司的薪水,目前已经得到的数据是原公司关于职位,工作年限和薪水之间的数据,本例子中假定新人的工作年限是6.5年,用新人提供的16000的原薪水与模型预测的新人原来的薪水对比,确定新人提供信息的可信性.因此,数据整体作为训练集,用得到的模型对6.5处于的薪水水平进行预测,最终证明新人提供的薪水数据可信.

[3 分类](https://github.com/hanxinle/practical_machine_learning/tree/master/3_Classification)
  
  这部分数据模拟了SUV销售商对顾客信息的统计,要求将顾客根据是否对SUV有购买倾向将顾客分为两类.各种分类算法的思想如下:
  
* [Logistic Regression](https://github.com/hanxinle/practical_machine_learning/tree/master/3_Classification/Logistic_Regression)
  
  对数几率回归,这一模型有"阶跃"特性,不能理解为二分类算法的一种.本节所给的示例中,根据年龄\年收入判断用户是否会对SUV有购买倾向,几率超过50%即认为用户有购买倾向,反之则没有,进而根据模型预测结果对目标客户投放广告.
  
* [支持向量机SVM](https://github.com/hanxinle/practical_machine_learning/tree/master/3_Classification/%20Support%20Vector%20Machine%20(SVM))
  
  SVM可以视作两个类里面相隔最近的两个个体(support)之间选择一个分类边界,这两个个体到达这一边界的距离和是最大的,它是一个比数据空间少一维的超平面.SVM最特别的一点是,在两个类别里面最极端的个体具有不同于自身类别大多数个体的极端特征(二者往往特征相近),而SVM恰好是类别间最极端特例所得到的.
  
  
  
