import string

total = 0
currentstring = []
currentkey = []

while True:
    data = input("enter data")
    if data == "end":
        break
    for character in data:
        if character not in string.ascii_lowercase:
            currentstring.append(int(character))
    currentkey = (currentstring[0]*10)+currentstring[-1]
    ##print(currentkey)
    total += currentkey
    currentstring = []
    currentkey = []




print(total)
##print(currentstring)
##print(currentkey)