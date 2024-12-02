
score = 0
sys = {}

dirbuffer = []
currentdir = []
value = {}
filesize = 0
ls = False
while True:
    data = input("enter data ").split()
    if data[0] == "end":
        dirbuffer.append(currentdir)
        print(dirbuffer)
        print(sys)
        sys[dirbuffer[-3]][dirbuffer[-2]][dirbuffer[-1]] = value
        break

    if data[1] == "cd":

        if ls == True:
            dirbuffer.append(currentdir)
            if len(dirbuffer) == 1:
                sys[dirbuffer[-1]] = value
                value["size"] = filesize
            else:
                sys[dirbuffer[-2]][dirbuffer[-1]] = value
            ls = False
        currentdir = data[2]
        if sys == {}:
            sys[currentdir] = value
    elif data[1] == "ls":
        ls = True
        value = {}
        filesize = 0

    
    if ls == True and data[0] != "$":
        if data [0] != "dir":
            filesize += int(data[0])
            value["size"] = filesize
        else:
            value[data[1]] = data[0]
print(enumerate(sys))
print(dirbuffer)
print(sys)



