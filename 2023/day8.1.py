total = 0

current = 'AAA'
end = 'ZZZ'
map = []
mapinput = []
movement = 'LRLRLLRLLRRRLRLLRRLRLRRLRRLLLLRRLLRLRRLRRLRLRLRRLRLLRLRLRLRRRLLRLRLRLRRLRRLRRRLRRLRRLRRLRRLRRRLRRLRLLRLLRRRLRLRLLRRRLLRRLLLLRLRRRLLRLRLRRLRRRLRLRRLRLRRLLRLRRLLRLLRRLRLLRLLRRLRRRLLRRLRLRLRRLRRLRRRLRRLRRRLLRRLRLRRRLRRRLRLRRRLRRLRRLRRLRRRLRRLRLRRRLRLRRLLRRLRRRLRLRRRLLRLRRRLRRRLRLRLRRRLLRRLLRLRRRLRRLRRRLLLRRRR'
n = 0
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
    map.append(mapinput)

while n < len(movement):    
    test = [i for i in map if i[0] == current]
    mapinput = test[0]
    if movement[n] == 'L':
        current = mapinput[1]
    else:
        current = mapinput[2]
    n += 1
    total += 1
    if n == len(movement):
        n = 0
    if current == end:
        break

print(total)

