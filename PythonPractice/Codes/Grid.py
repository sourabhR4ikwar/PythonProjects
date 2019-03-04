def column():
    print("|",end=" ")
    print("  "*4,end="")
    print("|",end=" ")
    print("  "*4,end="")
    print("|")


def row():
    print("+",end=" ")
    print("- "*4,end="")
    print("+",end=" ")
    print("- "*4,end="")
    print("+")

def displayGrid():
    row()
    column()
    column()
    column()
    column()
    row()
    column()
    column()
    column()
    column()
    row()

displayGrid();
