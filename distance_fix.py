import re

old = open("500miledistance.csv", "r")
new = open("500milefixed.csv", "w")
old.readline() # skip init line
line = old.readline()
currLine = re.split(r',', line)
currZip = currLine[0]

# init 1st line
new.write(currLine[0].strip(""))
new.write(',')
new.write(currLine[1].strip(""))
new.write(',')
new.write(currLine[2].strip("").rstrip())
new.write(',')

for x in old:
    newLine = re.split(r',', x)

    if currZip != newLine[0]:
        new.write('\n')

        new.write(newLine[0].strip(""))
        new.write(',')
        new.write(newLine[1].strip(""))
        new.write(',')
        new.write(newLine[2].strip("").rstrip())
        new.write(',')

        currZip = newLine[0]
        #print(currZip)
    
    elif float(newLine[2].strip("").rstrip()) < 201:
        new.write(newLine[1].strip(""))
        new.write(',')
        new.write(newLine[2].strip("").rstrip())
        new.write(',')

old.close
new.close
