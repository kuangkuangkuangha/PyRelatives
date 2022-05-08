i = raw_input()
res = {}
res["LETTERS"] = 0
res["DIGITD"] = 0
for j in i:
    if '0'<=j<='9':
        res["DIGITD"] = res["DIGITD"] + 1
    elif 'a'<=j<='z' or 'A'<=j<='Z':
        res["LETTERS"] += 1

print("LETTERS {0}\nDIGITS {1}".format(res["LETTERS"],res["DIGITD"]))
