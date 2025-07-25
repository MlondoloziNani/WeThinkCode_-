greeting = input("Greeting: ").lower().lstrip().split(" ")[0]
greeting = greeting.replace(",","")
check_h = greeting[0]

if greeting == "hello":
    print("$0")
elif check_h == "h":
    print("$20")
else:
    print("$100")
