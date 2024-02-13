aple = dict(er=33, d=4, cd=3)
ball = {1:'a', 2:'b', 3:'79'}
dic1 = {"a":aple, "b":ball, "c":"cake", "d":"diamond", False:"ложь", True:"правда", (1,2,3):[1,2,3], 5:5.00}


dic1.popitem()
dic1.pop('d')
dic1["c"] = 'cray'
print(dic1)


print(dic1["a"])
print(dic1["a"]['er'])
print(dic1[(1,2,3)])
print(dic1[(1,2,3)][1])
print(dic1["b"])
print(dic1["b"][3])
print(dic1[True])