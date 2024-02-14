# import math
# from time import sleep
# import platform
# import main as m

# m.printSome(m.summa(3, 20, 50, 7))

# # print(platform.platform())
# # print(platform.system())
# # print(platform.release())

# sleep(2)

# res = math.pow(4, 2)
# print(res)

#2
'''
class USER:
    #pass
    name = None
    email = None
    login = None
    age = None

    def __init__(self, name, email, login, age) -> None:
        self.setINFO(name, email, login, age) #self in function
        self.getINFO()
       
        # self.name = name
        # self.email = email
        # self.login = login
        # self.age = age

    def setINFO(self, name, email, login, age):
        self.name = name
        self.email = email
        self.login = login
        self.age = age

    def getINFO(self):
        print(f"Name: {self.name}. Email: {self.email}. Login: {self.login}. Yor age: {self.age}")



admin = USER('Admin', "adm@mail.ru", "addd", 29)
bob = USER('Bob', "bob@mail.ru", "booob", 19)
alex = USER('Alex', "al@mail.ru", "alexx", 34)

# admin.setINFO('Admin', "adm@mail.ru", "addd", 29)
# bob.setINFO('Bob', "bob@mail.ru", "booob", 19)
# alex.setINFO('Alex', "al@mail.ru", "alexx", 34)


# alex.getINFO()
# admin.getINFO()
# bob.getINFO()


# admin.login = 'Admin'
# bob.login = 'Bob'
# alex.login = 'Alex'

# print(admin.login)
# print(bob.email)
'''
'''
class Iz000:
    Izin = None
    P1 = None
    P2 = None
    P3 = None
    P4 = None

    def __init__(self, Izin, P1, P2, P3):
        self.Izin = Izin
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3
        self.get_info()
        
    def get_info(self): # self на оборот не проставил.. ппц
        i = "YES" if self.Izin else "NON"
        print(f" Izing: {i}, P1: {self.P1}, P2: {self.P2}, P3: {self.P3}")

class PI1(Iz000): #во всех подклассах не выводится число установленное значение для него ниже. вывод - None. изначальный параметр...
    P4 = None
    def __init__(self, Izin, P1, P2, P3, P4):
        self.Izin = Izin
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3
        self.get_info()
        self.P4 = P4
        # super(PI1, self).__init__(Izin, P1, P2, P3)#super(super strong)
        # self.P4 = P4
    def get_info(self):
        super().get_info()
        print(f"P4: {self.P4}")
        

class PI2(Iz000):
    P5 = None
    def __init__(self, Izin, P1, P2, P3, P5):
        super(PI2, self).__init__(Izin, P1, P2, P3)# roditel
        self.P5 = P5
    def get_info(self):
        super().get_info()
        print(f"P5: {self.P5}")


class PI3(Iz000):
    P6 = None
    
    def __init__(self, Izin, P1, P2, P3, P6):
        super().__init__(Izin, P1, P2, P3)# "PI3,"
        self.P6 = P6
    def get_info(self):
        super().get_info()
        print(f"P6: {self.P6}")


Iz1 = PI1(True, 1, 2, 3, 4)
Iz2 = PI2(False, 10, 20, 30, 50)
Iz3 = PI3(True, 11, 22, 33, 66)

Iz1.P4 = 44


# print(Iz1.Izin)
# print(Iz2.Izin)
# print(Iz2.P1)
# print(Iz3.P3)
'''


class Same ():
    pass

print(dir(int()))