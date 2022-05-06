words = raw_input()
res = {}
res["UPPER CASE"] = 0
res["LOWER CASE"] = 0
for i in words:
    if( i.islower() ):
        res["LOWER CASE"]+=1
    elif( "A"<=i<="Z"):
        res["UPPER CASE"]+=1

print("UPPER CASE {0}\nLOWER CASE {1}".format(res["UPPER CASE"], res["LOWER CASE"]))