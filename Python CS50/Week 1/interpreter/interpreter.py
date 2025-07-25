def main():
    x, y, z = input("Expression: ").split(" ")
    x = float(x)
    z = float(z)

    if y == "+":
        print(round(add(x,z), 1))
    elif y == "-":
        print(round(subtract(x,z), 1))
    elif y == "*":
        print(round(multiply(x,z), 1))
    else:
        print(round(divide(x,z), 1))


def add(x,z):
    return x + z

def subtract(x,z):
    return x - z

def multiply(x,z):
    return x * z

def divide(x,z):
    return x / z


main()
