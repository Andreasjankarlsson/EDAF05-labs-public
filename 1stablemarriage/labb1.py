
textFile = open("1stablemarriage/data/sample/1.in", 'r')
lines = textFile.readlines()
print(lines)
count = 0
for line in lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))



