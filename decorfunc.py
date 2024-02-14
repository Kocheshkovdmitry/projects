def auth(funcret):
    def wrapper():
        isAuth = True
        if (not isAuth):
            funcret()
        else:
            print('You non registr!')
            funcret()
    return wrapper
def test(funcret1):
    def wrapper():
        print('Befor')
        funcret1()
        print('After')
    return wrapper
@test
@auth
def show():
    print('Print show')


show()