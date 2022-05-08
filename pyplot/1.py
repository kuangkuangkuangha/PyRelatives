import  matplotlib.pyplot as plt
import numpy as np
#导入包
x=np.linspace(-3,3,50)#产生-3到3之间50个点
y1=2*x+1#定义函数
y2=x**2

# 绘制直线
plt.figure(num=10086, figsize=(10, 5))  # 展示图片的名字，长宽设置
plt.plot(x,y1)

plt.show()