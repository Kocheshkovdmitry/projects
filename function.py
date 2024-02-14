# def testpr():
#     print('some money')
#     #pass

# testpr()

# def testpr(gr):
#     print(gr, '!', sep='')
#     #pass

# same = 'WORLD'
# testpr(same)

# def add(x ,y, additonal = 0):
#     res = x + y + additonal
#     testpr(res)
#     return res

# add(2, 3)
# num1 = int(input('Enter number1:'))
# num2 = int(input('Enter number2:'))
# res = add(num1, num2, 10)
# print(res)


# def mult(x, y, *args):
#     print(x, y, args)#*

# mult(3, 4, 5, 'wer', True, 4556, 'nin')

# def mult(*args):
#     for i in args:
#         print(f"Element: {i}")
# mult(3, 4, 5, 'wer', True, 4556, 'nin')

# def mult(**kargs):
#     for keys, value in kargs.items():
#         print(f"Keys: {keys} Element: {value}")

# mult(x = 5, y = 5, qwerty = 'ytrewq', onliworld = 55)

# data_used = dict(a = 1, b = 10, c = -13, d = 34, g = 23)
# minel = 1000
# for k, v in data_used.items():
#     if v < minel:
#         minel = v
# print(f'mini: {minel}')

# data_used2 = dict(a = 1, b = 10, c = 13, d = 34, g = 23)
# minel = 1000
# for k, v in data_used2.items():
#     if v < minel:
#         minel = v
# print(f'mini: {minel}')


# def minimal(min):
#     minel = 1000
#     for k, v in min.items():
#         if v < minel:
#             minel = v
#     print(f'mini: {minel}')# отступы
#     return minel
# data_used = dict(a = 1, b = 10, c = -13, d = 34, g = 23)
# data_used2 = dict(a = 1, b = 10, c = 13, d = 34, g = 23)

# min1 = minimal(data_used)
# min2 = minimal(data_used2)

# if min1 < min2: print(min1)
# else: print(min2)


#lambda

lam1 = lambda x, y, z: (x + y) * z

print(lam1(5, 7, 2))