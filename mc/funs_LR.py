import numpy as np

# 激活函数
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 损失函数
def cost(w, X, y):
    w = np.matrix(w)
    X = np.matrix(X)
    y = np.matrix(y)

    # first 和 second 只不过是代价函数公式的链各个部分
    first = np.multiply(-y, np.log(sigmoid(X * w.T)))
#    print("***111***" + str(sigmoid(X * w.T)))
#    print("***111***" + str(np.log(sigmoid(X * w.T))))
    second = np.multiply((1 - y), np.log(1 - sigmoid(X * w.T)))
#    print("***222***" + str(sigmoid(X * w.T)))
#    print("***222***" + str(np.log(1 - sigmoid(X * w.T))))

# 其实返回的就是某一次样本，[x1, x2, x3...](房子面积， 卧室书)推测出来的放假 与 真实放假之间的差值
    return np.sum(first - second) / (len(X))  # 这是➗m

# 正则化函数
def costReg(w, X, y, learningRate):
    w = np.matrix(w)
    X = np.matrix(X)
    y = np.matrix(y)
    first = np.multiply(-y, np.log(sigmoid(X * w.T)))
    second = np.multiply((1 - y), np.log(1 - sigmoid(X * w.T)))
    reg = (learningRate / (2 * len(X))) * np.sum(np.power(w[:, 1:w.shape[1]], 2))
    return np.sum(first - second) / len(X) + reg


