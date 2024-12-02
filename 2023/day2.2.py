total = 0

while True:
    r = []
    g = []
    b = []
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
                r.append(int(chunkcheck[i].replace(" red", "")))
            if "green" in chunkcheck[i]:
                g.append(int(chunkcheck[i].replace(" green", "")))
            if "blue" in chunkcheck[i]:
                b.append(int(chunkcheck[i].replace(" blue", "")))
            i += 1
        n += 1
        
    if n == stop:
        total += max(r)*max(g)*max(b)
    
print(total)