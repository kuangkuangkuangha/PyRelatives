res = []
i = raw_input().split(',')
for j in i:
    inti = int(j, 2)
    if inti%5==0:
        res.append(j)
print(','.join(res))
