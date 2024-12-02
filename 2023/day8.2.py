from math import gcd

total = 0
vibecheck = []
totals = []
current = []
end = []
map = []
mapinput = []
movement = 'LR'
n = 0
m = 0
while True:
    data = input("enter data")
    if data == "end":
        break
    p1 = data.replace("=","") 
    p2= p1.replace("(","") 
    p3 = p2.replace(")","")
    p4 = p3.replace(",","")
    mapinput = p4.split(" ")
    del(mapinput[1])
    if mapinput[0][2] == 'A':
        current.append(mapinput[0])
    if mapinput[0][2] == 'Z':
        end.append(mapinput[0])
    map.append(mapinput)

while n < len(movement):    
    test = [i for i in map if i[0] == current[m]]
    mapinput = test[0]
    if movement[n] == 'L':
        current[m] = mapinput[1]
    else:
        current[m] = mapinput[2]
    n += 1
    total += 1
    if n == len(movement):
        n = 0
    if current[m] in end:
        totals.append(total)
        total = 0
        m += 1
        vibecheck.append(1)
    if len(vibecheck) == len(current):
        break

lcm = 1
for i in totals:
    lcm = lcm*i//gcd(lcm,i)
print(lcm)


