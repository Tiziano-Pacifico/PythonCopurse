fileslist = ["a.txt","b.txt","c.txt"]
path = "..\\textfiles\\"
for file in fileslist:
    f = open(path + file,"r")
    print(f.read())
    f.close()