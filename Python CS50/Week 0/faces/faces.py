def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")

    return str


def main():
    str = input()
    print(convert(str))


main()
