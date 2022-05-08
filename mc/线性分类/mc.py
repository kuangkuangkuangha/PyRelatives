from sklearn import datasets
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data[:100,:]
y = iris.target[:100]
print("样本数据：",X)
print("样本target分类：", y)

import numpy as np
vec_ones = np.ones(len(X))
X_aug = np.c_[vec_ones.T, X]


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_aug, y, random_state =12, stratify=y, test_size =0.3)
# train_target：所要划分的样本结果
# test_size：样本占比，如果是整数的话就是样本的数量
# random_state：是随机数的种子。

from funs_LR import sigmoid, cost

maxIters = 200
stepLength = 0.01  # 每次梯度下降的步长

w = np.random.rand(X_train.shape[1])  # 随机初始化一组参数w（1*5）,相当于五个属性的权重
print("X_train.shape[1]:", w)

print("init loss: " + str(cost(w, X_train, y_train)))  # 第一次loss值随机初始化
perLoss = cost(w, X_train, y_train)  # 得到[w1, w2, w3...]权重的情况下 预测房价和真实放假之间的差距

for index in range(maxIters): # 迭代200次
	des_w = np.dot(X_train.T, (sigmoid(np.dot(X_train, w)) - y_train)) / len(X_train)
	# 这里开始利用梯度下降，宏观的看通过这里可以得到一个w的调整的值（利用的是最大似然函数，要深究一下）
    # dot()用于矩阵乘法

	w = w - stepLength * des_w  # 通过上面得到的调整的值和步长，更新新的参数w

	print("after iter[" + str(index) +"]: " + str(cost(w, X_train, y_train)))  
	# 更新w后再一次计算和真实放假之间之间的差距，可以发现确实是减小了
	curLoss = cost(w, X_train, y_train)
    
	print(str(np.absolute(curLoss - perLoss))) # absolute取绝对值

	# 然后重复迭代200次，直到差距小于我们的预期值的时候，[w1, w2, w3...]就可以算得上调整好了
	if (np.absolute(curLoss - perLoss) < 1e-6) or (curLoss < 1e-4): #1*10的-6次方
		break
	
	perLoss = curLoss


# 这里就是用调整好的[w1, w2, w3...]进行预测测试集
pred = sigmoid(np.dot(X_test, w))
pred[pred >= 0.5] = 1
pred[pred < 0.5] = 0
pred = pred.astype(int)
errorRate = 1.0 * np.sum(np.absolute(pred - y_test)) / len(X_test) # 计算错误率
print("错误率是：", errorRate)
