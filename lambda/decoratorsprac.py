def decorc(x):
    def inner():
        result = x()
        return result * 2

    return inner

@decorc
def num():
    return 5

print(num())
