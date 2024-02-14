#i = 0
#while i < 10:

#    print(f"Element: {i}")
 #   i += 1  


# i1 = True
# while i1:
#     user = int(input('Enter number zero:'))
#     if user == 0:
#         i1 = False
# print('Very good!')

# for i in range(2, 10, 2):
#     print(f"Element: {i}")

# word = 'Good!'
# for el in word:
#     if el == 'o': print("Found")

# for i in range(10, 20):
#     if i % 2 == 0: continue
#     print(f'Element: {i}')
#     if i == 15: break

# word = 'Good!'
# for el in word:
#     if el == 'o':
#         print("Found")
#         break
# else: print('NON')

# sp1 = (5, 15, 6.4, True, 'hello', [5.2, 5.3, 5.4])

# for el in sp1:
#     print(f'Element: {el}')

# sp1 = {5, 15, 6.4, True, 'hello'}
# for el in sp1:
#     print(f'Element: {el}')

# sp1 = {'name': 'Anna', 'age': 25, (5, 6): 56, True:100, False:-100}
# for el in sp1:
#     print(f'Element: {el}')

# sp1 = {'name': 'Anna', 'age': 25, (5, 6): 56, True:100, False:-100}
# for keys, valu in sp1.items():
#     print(f'Keys: {keys}. Element: {valu}')
# user_data = []

# namber1 = int(input('Enter number:'))
# for i in range(namber1):
#     el = int(input('Enter value:'))
#     user_data.append(el)
# print(user_data)

# maxel = 0
# for i in user_data:
#     if i > maxel:
#         maxel = i
# print('Max element:', maxel)

user_list = 'skate,footbol,painting'
user_list1 = user_list.split(',')
user_vis = []
for i in user_list1:
    user_vis.append(i.capitalize())
user_vis_fin = ', '.join(user_vis)
print(user_vis_fin)