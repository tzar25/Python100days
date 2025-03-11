
def pyramid(n: int):
    for i in range(n):
        print(" " * (n-i-1) + "#" * (i+1), end="")
        print("  ", end="")
        print("#" * (i+1))


pyramid(4)
