import re

distances = open("500milefixed.csv", "r")
customers = open("customers.txt", "r")
fsl = open("fsl.txt", "r")
match = open("match.csv", "w")

# populate fsl dictionary
fsldict = {}
for f in fsl:
    fZip = re.split(r'\t', f)
    fsldict[fZip[1].rstrip()] = fZip[0]

q = 0
# search for zipcodes
for c in customers:
    distances.seek(0)
    distances.readline()
    cZip = re.split(r'\t', c)
    closest = "NULL"
    distance = 1000000

    if cZip[0][0:5] in fsldict:
        distance = 0
        closest = fsldict[cZip[0][0:5]]


    elif cZip[1] != "#N/A\n" and int(cZip[1]) < 5:
        flag = 0
        for d in distances:
            dZip = re.split(r',', d)
            if dZip[0][1:6] == cZip[0][0:5]:
                for i in range(0, int((len(dZip) - 1) / 2), 1):
                    #print(dZip[(i * 2) + 1][1:6])
                    if dZip[(i * 2) + 1][1:6] in fsldict: 
                        #print("babboo")
                        if float(dZip[(i * 2) + 2]) < distance:
                            distance = float(dZip[(i * 2) + 2])
                            closest = fsldict[dZip[(i * 2) + 1][1:6]]
                            flag = 1
                    elif flag:
                        break
            elif flag:
                break



    match.write(cZip[0][0:5])
    match.write(',')
    match.write(cZip[1].rstrip())
    match.write(',')
    match.write(closest)
    match.write(',')
    match.write(str(distance))
    match.write(',')
    match.write('\n')

    if q % 50 == 0:
        print(q)
    q = q + 1

distances.close
fsl.close
customers.close
match.close