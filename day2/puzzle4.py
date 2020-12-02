
file = open("input.txt", "r")

entries = []

"""parse input"""
for line in file :
    entry = []
    
    index = line.find("-")
    
    entry.append(line[:index])
    
    line = line[index+1:]
    
    index = line.find(" ")
    
    entry.append(line[:index])
    
    line = line[index+1:]
    
    index = line.find(":")
    
    entry.append(line[:index])
    
    line = line[index+2:-1]
    
    entry.append(line )
    
    entries.append(entry)
    
file.close()

"""check if password satisfies given requirements"""
def checkPass (entry) -> bool :
    firstPos = int(entry[0]) - 1
    secondPos = int(entry[1]) - 1
    
    checkFor = entry[2]
    
    password = entry [3]
    
    count = 0
    if firstPos  < len(password) and password[firstPos] == checkFor :
        count += 1    
    if secondPos < len(password) and password[secondPos] == checkFor :
        count+= 1
        
    if count == 1 :
        return True
    return False

count = 0
for entry in entries :
    if checkPass(entry) :
        count += 1

print (f"There were {count} valid passwords.")











    