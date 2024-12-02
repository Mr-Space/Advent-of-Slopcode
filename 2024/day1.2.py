n = 0
total = 0
a = []
b = []

while True:
    data = input("enter data")
    if data == "end":
        break
    data2 = data.split("   ")
    a.append(int(data2[0]))
    b.append(int(data2[1]))

a.sort()
b.sort()

while n != len(a):
    x = b.count(a[n])
    similar = a[n]*x
    total += similar
    n += 1

print(total)