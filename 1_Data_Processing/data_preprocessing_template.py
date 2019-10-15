# 本文件为数据处理的流程模版文件,不需要的部分请注释

# 引用必要的库
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 导入数据库
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, 3]

# 处理缺失数据

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X.iloc[:, 1:3])
X.iloc[:, 1:3] = imputer.transform(X.iloc[:, 1:3])

# 虚拟编码(自变量和因变量都需要)
# 自变量部分
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

# 因变量部分
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# 数据分为训练集和验证集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# 特征缩放

'''from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)'''
