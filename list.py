sp1 = [1, 5.5, "word", True, "5", 1496, [16, 97, 700, 699]]
sp1[0] = 44

print(sp1[-1][2])
sp1.append("ins")
sp2 = [3,7,5,9,11]
sp1.extend(sp2)
sp1.insert(1, 7.6)

sp1.remove(5.5)
sp1.pop(-1)

sp2.sort()


print(sp1)
sp1.reverse()
#sp1.clear()
print(sp1.count(5))
print(sp1)
print(sp2)
print(len(sp1))
print(sp1[:])
print(sp1[5:-1])
print(sp1[5:-1:2])


sp3 = list("world world all")
sp3[0] = "T"
print(sp3)
print(sp3.count('w'))
sp4 = ('world world')
print(len(sp4))
print(sp4.upper())
print(sp4.find('r'))
p4 = ('world world')
print(sp4.lower())
