
score = 0

rock = ["A", "X"]
paper = ["B", "Y"]
scissors = ["C", "Z"]
while True:
    x, y = input("enter data").split()
    
    if x == 'end':
            break
    if y == "X":
        score += 1
    elif y == "Y":
        score += 2
    elif y == "Z":
        score += 3
    
    if x in rock and y in rock:
        score += 3
    elif x in paper and y in paper:
        score += 3
    elif x in scissors and y in scissors:
        score += 3    
    else:
        if y in rock and x in scissors:
            score += 6
        elif y in paper and x in rock:
            score += 6
        elif y in scissors and x in paper:
            score += 6
    
print(score)


    
