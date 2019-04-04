fin = open("words.txt")

def has_no_e(word):
    if 'e' in word:
        return False
    else :
        return True
size = 0
numOfE = 0
for line in fin:
    word = line.strip()
    size = size + 1
    if has_no_e(word):
        print(word)
        numOfE = numOfE + 1

print("Percentage of no E words ", (numOfE/size)*100)
