maximum = None
minimum = None

while True:
    try:
        inp = input("Enter a number: ")
        if inp == "done":
            break
        inp = int(inp)
        if maximum == None or inp > maximum:
            maximum = inp
        if minimum == None or inp < minimum:
            minimum = inp
    except:
        print("Invalid input")
print(maximum, minimum)
