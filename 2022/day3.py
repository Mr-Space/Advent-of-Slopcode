import string

score = 0
values = list(string.ascii_lowercase + string.ascii_uppercase)

while True:
    data = input("enter data")
    if data == "end":
        break
    sack1 = data[:len(data)//2]
    sack2 = data[len(data)//2:]
    print(sack1,sack2)
    common = list(set(sack1)&set(sack2))
    score += (values.index(' '.join(common)) + 1)
    
print(score)
