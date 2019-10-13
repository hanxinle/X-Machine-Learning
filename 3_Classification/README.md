# 机器学习任务-分类
  
  这一类分类任务中,其输出值是整数,整数标志的是目标的种类.本章提供了一个分类问题常用的程序模版.
  
  本章的任务是:根据年龄\年收入判断用户是否会对SUV有购买倾向,有购买倾向则对其推送SUV广告.
  
  常见的分类算法有以下几种:
    

* [Logistic Regression](https://github.com/hanxinle/practical_machine_learning/tree/master/3_Classification/Logistic_Regression)

    不少人把Logistic Regression称为“逻辑回归”，但实际上logistic和中文“逻辑”(logic) 没半毛钱关系。LR是广义线性模型，把线性回归y=w^T x的y换成ln[p/(1-p)]即得，p是p(y=1|x)。p/(1-p)是“几率”，所以LR应称为“对数几率回归”.(引自微博:南大周志华)

    在<机器学习实战>中已经有所提及,引入该方法的目的是借用S函数的"阶跃"的性质,实际上,在本节所给的示例中,根据年龄\年收入判断用户是否会对SUV有购买倾向也是利用了这一性质,超过50%即认为用户有购买倾向,反之则没有,进而根据模型预测结果对目标客户投放广告,该方法不能理解为二分类.

* [支持向量机SVM](https://github.com/hanxinle/practical_machine_learning/tree/master/3_Classification/%20Support%20Vector%20Machine%20(SVM))

    这一方法,可以视作两个类里面相隔最近的两个个体(support)之间选择一个分类边界,这一边界到达上述两个个体的距离是最大的,它是一个比数据空间少一维的超平面.SVM最特别的一点是,在两个类别里面最极端的个体具有不同于自身类别大多数个体的极端特征(二者往往特征相近),而SVM恰好是类别间最极端特例所得到的.

* [带核函数的支持向量机Kernel_SVM](https://github.com/hanxinle/practical_machine_learning/tree/master/3_Classification/Kernel%20SVM)

    在数据表现为线性不可分的情况下,依旧可以采用低维到高维的投射SVM方法,在高维空间中使得数据变得可分,再将分类好的数据映射到原来的维度.在采用高斯核的时候,分子上的常数为核中心,这里的值在高维空间较大,而分母的值控制的是高斯核的半径.其它核函数还有S函数,二元多项式函数,[这里](http://crsouza.com/2010/03/17/kernel-functions-for-machine-learning-applications/)提供一个网站,对核函数方法进一步介绍.
    
* [朴素贝叶斯分类器Naive Bayes](https://github.com/hanxinle/practical_machine_learning/tree/master/3_Classification/Naive%20Bayes)

     贝叶斯公式中,所求的概率往往是无法直接观察得到的,而等号右边的各项比较容易得到.朴素贝叶斯中"朴素"表征所有数据的特征是独立的(特征之间不会互相影响),这一假设会有误差,但是降低了解决问题的难度.对右边分母P(x)又称似然,在二维求解的时候,通过在新引入数据周围画圈来对其进行求解,同时求得的还包括分子上的条件概率值.应用这一方法时,分母值相同,这个似然值作为分母是可以省略的.

* [决策树](https://github.com/hanxinle/practical_machine_learning/tree/master/3_Classification/%20Decision%20Tree%20Classification)

     在算法没有使用欧式距离时,不需要的使用特征缩放.本例子中,为了后面画图的方便,进行了特征缩放,算是小小的妥协.决策树容易产生过拟合,不能忽略训练集中的噪音.
     
* [随机森林](https://github.com/hanxinle/practical_machine_learning/tree/master/3_Classification/%20Random%20Forest%20Classification)

     随机森林首先从数据集中选择K个数据放入自身训练集,然后用这些数据训练决策树分类器,第三步重复上述两步过程,得到一定数量的决策树算法.对新的数据点,用所得到的决策树分类算法分别对其进行分类,选择多数决策树得到的类别作为随机森林算法的类别. 这一算法依旧会出现过拟合.
     
*  [本章小节]

     对每种分类算法优缺点的总结,对分类算法模型性能评估的方法介绍,针对不同任务时不同分类算法取舍及提升模型性能的方法概述.
     
     在这个分类任务中,基于核方法的SVM和贝叶斯分类曲线平滑,且没有过拟合现象,其分类结果好于决策树和随机森林算法.这不说明几种算法的优劣,实际上,算法性能和数据质量\特征\任务类型\参数设置等因素有关.
