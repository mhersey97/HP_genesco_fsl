import re

fsl = open("fsl.txt", "r")
match = open("match.csv", "r")
out = open("out.csv", "w")

for f in fsl:
    sl = re.split(r'\t', f)[0]
    count = 0

    match.seek(0)
    for m in match:
        site = re.split(r',', m)[2]
        if site == sl:
            count += 1
    
    out.write(sl)
    out.write(',')
    out.write(str(count))
    out.write(',')
    out.write(str(float(3 * count * 0.05)))
    out.write('\n')

fsl.close
match.close
out.close
