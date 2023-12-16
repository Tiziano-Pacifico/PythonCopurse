import glob

myfiles = glob.glob("C:\\Users\\Tiziano Pacifico\\PycharmProjects\\cap2\\Exercises\\*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())