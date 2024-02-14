# f = open('testfile.txt', 'a')
# userworld = input('Enter yor name:') 
# f.write(userworld + '\n')
# f.close()

# f = open('testfile.txt', 'r')
# print(f.read(100))
# f.close()

# f = open('testfile.txt', 'r')
# for line in f:
#     print(line, end='')
# f.close()

# try:
#     num = int(input('Enter number:'))
#     print(num)
# except ValueError:
#     print('ENTER NUMBER SIMBOL')

# userD = False
# while not userD:
#     try:
#         num = int(input('Enter number:'))
#         userD = True
#         print(num)
#     except ValueError:
#         print('ENTER NUMBER SIMBOL')
# uaerd = False
# while not uaerd:
#     try:
#         numf = int(input('Enter number file:'))
#         f = open(f'testfile{numf}.txt', 'r')
#         uaerd = True
#         print(f.read())

#         f.close()
#     except FileNotFoundError:
#         print('file non')
#     except ValueError:
#         print('NUMBER!!!')
#     finally:
#         print('Finish')

uaerd = False
while not uaerd:
    try:
        numf = int(input('Enter number file:'))
        with open(f'testfile{numf}.txt', 'r') as f:
            uaerd = True
            print(f.read())
    except FileNotFoundError:
        print('file non')
    except ValueError:
        print('NUMBER!!!')
    finally:
        print('Finish')