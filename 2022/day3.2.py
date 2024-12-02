import string

score = 0
values = list(string.ascii_lowercase + string.ascii_uppercase)
s1 = []
s2 = []
s3 = []
while True:
    data = input("enter data")
    if data == "end":
        break
    if s1 == []:
        s1 = data[:len(data)]
    elif s2 == []:
        s2 = data[:len(data)]
    else:
        s3 = data[:len(data)]
    while s1 and s2 and s3 != []:
        common = list((set(s1)&set(s2))&set(s3))
        score += (values.index(' '.join(common)) + 1)
        s1 = []
        s2 = []
        s3 = []
        break
    
    
print(score)