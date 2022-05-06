lst = []
while True:
    i = raw_input()
    if (i):
        lst.append(i.upper())
    else:
        break

for s in lst:
    print(s)