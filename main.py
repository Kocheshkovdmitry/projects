if __name__ == "__oop__":
    print('Hello world!')

some = 15

def printSome(word):
    print(f"Result: {word}")

def summa(*arg):
    sum = 0
    for i in arg:
        sum += i
    return sum
