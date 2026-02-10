# Get height of pyramid from user
height = 0

while (height < 1 or height > 8):
    try:
        height = int(input("Height: "))
    except ValueError:
        print("Enter a number between 1 and 8, inclusive.")
        height = int(input("Height: "))


for i in range(height):
    # Loops for left-side of pyramid
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("#", end="")

    # Gap between left- and right-side of pyramid
    print("  ", end="")

    # Right-side of pyramid (no need to add spaces!)
    for r in range(i + 1):
        print("#", end="")

    # New row
    print("")
