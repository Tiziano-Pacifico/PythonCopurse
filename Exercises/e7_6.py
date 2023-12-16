filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    print(filename)
    file = open(filename, "w")
    file.write("Hello")
    file.close()