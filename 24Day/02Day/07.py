i = input()
j = input()
res = []
for m in range(0, i):
    temp = []
    for n in range(0, j):
        temp.append(m*n)
    res.append(temp)

print(res)

# list索引用法
# kk = ["hah", "nihao", "bye"]
# for i in kk:
#     print(i)

# print("\b")

# for j in range(0, 3):
#     print(kk[j])
