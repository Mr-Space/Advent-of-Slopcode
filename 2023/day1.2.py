import string

total = 0
currentstring = []
currentkey = []


while True:
    data = input("enter data")
    if data == "end":
        break
    stop = len(data) + 1
    n = 0
    while n < stop:
        vibecheck = data[n:n+5] 
        check1 = vibecheck.replace("one","1")
        check2 = check1.replace("two","2")
        check3 = check2.replace("three","3")
        check4 = check3.replace("four","4")
        check5 = check4.replace("five","5")
        check6 = check5.replace("six","6")
        check7 = check6.replace("seven","7")
        check8 = check7.replace("eight","8")
        check9 = check8.replace("nine","9")
        for character in check9:
            if character not in string.ascii_lowercase:
             currentstring.append(int(character))
        n += 1
    currentkey = (currentstring[0]*10)+currentstring[-1]
    ##print(currentkey)
    total += currentkey
    check9 = []
    currentstring = []
    currentkey = []
    n = 0



print(check9)
print(total)
##print(currentstring)
##print(currentkey)