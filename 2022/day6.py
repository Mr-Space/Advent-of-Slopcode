
data = input("enter data")
a = 0
while True:
    chk = data[a:(a+4)]
    x = chk.count(chk[0])
    y = chk.count(chk[1])
    z = chk.count(chk[2])

    if x+y+z > 3:
        a += 1
    else:
        break
    
print(a+4)