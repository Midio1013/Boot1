
l1 =[90 ,68 ,67 ,40 ,24 ,45 ,79 ,24 ,99 ,15]
_min =100
_max =0
allst =0
for i in range(len(l1)):
    if _min > l1[i]:
        _min =l1[i]
for i in range(len(l1)):
    if _max <l1[i]:
        _max =l1[i]
l1.pop(l1.index(_min))
l1.pop(l1.index(_max))
for i in l1:
    allst+=i
allst/=5
print(allst)
