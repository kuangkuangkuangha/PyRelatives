words = raw_input().split(' ')
a = list(set(words))
a.sort()
# sort( list(set(words)) ) 
print(' '.join(a))