
data = input("enter data")
a = 0
while True:
    chk = data[a:(a+14)]

    def unique(chk):
        for i in range(len(chk)):
            for j in range (i + 1, len(chk)):
                if(chk[i]==chk[j]):
                    return False
        return True
    
    if unique(chk):
        break
    else:
        a += 1
    
    
print(a+14)