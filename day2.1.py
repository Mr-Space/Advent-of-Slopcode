total = 0

while True:
    data = input("enter data")
    if data == "end":
        break
    data2 = data.split(" ")
    curreport = list(map(int, data2))
    chnglist = []
    for i in curreport:
        if curreport.index(i) == len(curreport)-1:
            if not (min(chnglist) < 0 < max(chnglist)):
                total += 1
            break
        change = curreport[curreport.index(i)+1] - curreport[curreport.index(i)]
        chnglist.append(change)
        if change < -3 or change > 3 or change == 0:
            break

print(total)
        
