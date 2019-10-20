# 实践机器学习

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

* [核方法支持向量机](https://github.com/hanxinle/practical_machine_learning/tree/master/3_Classification/Kernel%20SVM)

  在数据表现为线性不可分的情况下,依旧可以采用低维到高维的投射SVM方法,在高维空间中使得数据变得可分,再将分类好的数据映射到原来的维度.在采用高斯核的时候,分子上的常数为核中心,这里的值在高维空间较大,而分母的值控制的是高斯核的半径.其它核函数还有S函数,二元多项式函数,这里提供一个网站,对核函数方法进一步介绍.
  
* [朴素贝叶斯Naive Bayes](https://github.com/hanxinle/practical_machine_learning/tree/master/3_Classification/Naive%20Bayes)

  贝叶斯公式中,所求的概率往往是无法直接观察得到的,而等号右边的各项比较容易得到.朴素贝叶斯中"朴素"表征所有数据的特征是独立的(特征之间不会互相影响),这一假设会有误差,但是降低了解决问题的难度.对右边分母P(x)又称似然,在二维求解的时候,通过在新引入数据周围画圈来对其进行求解,同时求得的还包括分子上的条件概率值.应用这一方法时,分母值相同,这个似然值作为分母是可以省略的.
  
* [决策树](https://github.com/hanxinle/practical_machine_learning/tree/master/3_Classification/%20Decision%20Tree%20Classification)
  
  随机森林首先从数据集中选择K个数据放入自身训练集,然后用这些数据训练决策树分类器,第三步重复上述两步过程,得到一定数量的决策树算法.对新的数据点,用所得到的决策树分类算法分别对其进行分类,选择多数决策树得到的类别作为随机森林算法的类别. 这一算法依旧会出现过拟合.
  
* [分类算法的性能评估与改进](https://github.com/hanxinle/practical_machine_learning/blob/master/3_Classification/Evaluating%20Classification%20Models%20Performance.md)

  对每种分类算法优缺点的总结,对分类算法模型性能评估的方法介绍,针对不同任务时不同分类算法取舍及提升模型性能的方法概述.

  在这个分类任务中,基于核方法的SVM和贝叶斯分类曲线平滑,且没有过拟合现象,其分类结果好于决策树和随机森林算法.这不说明几种算法的优劣,实际上,算法性能和数据质量\特征\任务类型\参数设置等因素有关.

[4 集群](https://github.com/hanxinle/practical_machine_learning/blob/master/4_Clustering/README.md)

  集群（clustering）与分类（classification）虽然有许多相似之处，它们的核心思想大有不同。在集群中，我们并没有对数据的预期，也缺乏对数据结构的了解；我们的目标是把数据分成不同的群或类（cluster），使得在同一个类中的数据都有相似的属性。集群算法可以探测出人类直觉难以体察到的数据结构，并将其直接运用于集群聚类。

[5 关联规则](https://github.com/hanxinle/practical_machine_learning/tree/master/5_Apriori)

  在现实世界获取数据的时候,有时会发觉一个现象,即数据之间的存在某种关联,如用户的不同行为之间存在关联,如爱屋及乌,喜欢事务A总是伴随着对事务B的喜欢.
另一个经典的示例就是那个丈夫买了尿布,往往还会买啤酒,商场会发现尿布的销量和啤酒的销量是正相关的.如果数据类型增多,如何找出数据中的这类规律,就是先验算法的作用.

* [Apriori](https://github.com/hanxinle/practical_machine_learning/tree/master/5_Apriori)
  
  本章的例子是介绍一家法国杂货店如何利用关联规则如何提升自己的销售额,他们将商品间具有强提升度的商品放在一起,进而提升商品销量.

[6 强化学习](https://github.com/hanxinle/practical_machine_learning/tree/master/6_Reinforcement%20Learning)

   强化学习主要解决的问题是机器如何根据某一时刻的信息决定下一时刻需要采取的行动。强化学习也被运用在人工智能领域，比如说让机器人学习如何走路。机器在作出决策之后，如果得到期望的结果，机器会得到奖励，反之则会得到惩罚。通过这个试错的过程，机器可以学到如何对已有的信息作出决策。

  这一节的例子是商家投放了10个广告,每个广告代表一种商品使用场景,我们的任务是决定投放哪个广告.这个数据不仅仅是要求选中的广告的点击率最大,而且要针对第n个用户决定投放哪个广告,从而确保该广告的点击次数是最大的,数据来源并非投放广告前的统计,而是一种模拟数据,模拟了10000个用户对每个广告的点击情况.
  
* [置信区间上界 UCB](https://github.com/hanxinle/practical_machine_learning/tree/master/6_Reinforcement%20Learning/UCB)
* [Thompson抽样算法](https://github.com/hanxinle/practical_machine_learning/tree/master/6_Reinforcement%20Learning/Thompson_Sampling)
  
[7 降维](https://github.com/hanxinle/practical_machine_learning/tree/master/7_Dimensionality%20Reduction)

  在多元线性回归中所采用的技术是特征选择,特征选择减少的是自变量的个数,这一方法不对初始的数据集的数据进行更改.降维所得到的自变量不包含在原数据的自变量中,而是由数据的特性抽取得到的新的自变量.
  
  本章涉及两个算法PCA和kernel-pac.数据的自变量是不同红酒的多个化学成分,因变量是客户分类.参数p的确定取决与p能解释多少自变量的方差,需要在编码中先测试再选择函数赋值,初始值等于原自变量数量.本课程的例子确定了2个新自变量,可以拟合56%的方差.
  
[8 模型选择](https://github.com/hanxinle/practical_machine_learning/tree/master/8_Model%20Selection)

  这一章提到两个算法,交叉验证(Cross Validation)和网格搜索(Grid Search).交叉验证,是不改变超参数的情况下,通过数据集不同的划分,评估模型的性能.网格搜索是将所有可选参数带入模型,评估每个参数下的模型性能,确定最佳模型的参数设置.

  
