values = raw_input().split(',')
res = []
for i in values:
    if int(i)%2==1:
        res.append(str(int(i)*int(i)))

print(','.join(res))
