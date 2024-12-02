total = 1
winnar = []
speed = 0
while True:
    data = input("enter data")
    if data == "end":
        break
    splitdata = data.split(",")
    time = int(splitdata[0])
    distance = int(splitdata[1]) 
    while speed < time+1:
        currentdis = speed * (time-speed)
        if currentdis > distance:
            winnar.append(currentdis)
        speed += 1
    total = total*len(winnar)
    #winnar = []
    speed = 0
    
print(total)
print(len(winnar))