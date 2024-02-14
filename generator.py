
# def generator (num):
#     while num > 0:
#         yield num
#         num -=1

# val = generator(6)
# print(next(val))
# print(next(val))
# print(next(val))


def generator(lis):
    for i in lis:
        yield i

val = generator([6, [23, 17, 1], 15, 123, 7.6])

print(next(val))
print(next(val))
print('some taims')
print(next(val))