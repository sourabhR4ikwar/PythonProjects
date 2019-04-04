def count(n):
    if(n <= 0):
        print("Blast Off!")
    else:
        print(n)
        count(n-1)

count(8)
