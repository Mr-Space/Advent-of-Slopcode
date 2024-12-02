total = 0

while True:
    r = 0
    g = 0
    b = 0
    data = input("enter data")
    if data == "end":
        break
    splitdata = data.split("; ")
    datanumsplit = data.split(":",1)
    datanum = datanumsplit[0].replace("Game ", "")
    stop = len(splitdata)
    n = 0
    while n < stop:
        chunk = splitdata[n].split(": ")
        
        if n == 0:
            del chunk[0]
        chunkcheck = chunk[0].split(", ")
        i = 0
        while i < len(chunkcheck):

            if "red" in chunkcheck[i]:
                r = int(chunkcheck[i].replace(" red", ""))
            if "green" in chunkcheck[i]:
                g = int(chunkcheck[i].replace(" green", ""))
            if "blue" in chunkcheck[i]:
                b = int(chunkcheck[i].replace(" blue", ""))
            i += 1
        if r > 12 or g > 13 or b > 14:
            datanum = 0
            break
        else:
            n += 1
        
    if n == stop:
        total += int(datanum)
    
print(total)