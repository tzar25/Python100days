
ans = "n"

while True:
    val = ""
    if ans == "n":
        val += str(float(input("What is your first number? ")))
    else:
        val += x
    val += str(input('Pick an operation ("+", "-", "*" or "/") '))
    val += str(float(input("What is your second number? ")))
    x = str(eval(val))
    print(x)
    ans = input('Type "c" to continue with this number, "n" to start a new one or "q" to quit. ')
    if ans == "q":
        break




