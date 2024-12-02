score = 0

while True:
    e1, e2 = input("enter data").split(",")
    if e1 == "end":
        break
    r1, r2 = e1.split('-')
    r1, r2 = int(r1), int(r2)
    r3, r4 = e2.split('-')
    r3, r4 = int(r3), int(r4)

    e1r = list(range(r1,r2 + 1))
    e2r = list(range(r3,r4 + 1))
    
    common = list(set(e1r)&set(e2r))
    common.sort()
    if e1r == common or e2r == common:
        score += 1

print(score)