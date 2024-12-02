dirs = ['/']
dirsize = {'/'}
currentdir = []
currentsize = []
currenttotal = 0
ls = False
while True:
    data = input("enter data ").split()
    if data[0] == "end":
        break
    
    if data[1] == 'cd':
        data[2] = currentdir
        
    elif data[1] == 'ls':
        ls = True

    if ls == True:
        if data[0] == 'dir':
             dirs.append(data[1])
             currentsize.append(data[1])
        else:
            currenttotal += data[0] 
    
   

print(dirs)