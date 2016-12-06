"""
Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.
For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:
101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?
"""

def triangleCount(sequence):
    sequence = [x.strip() for x in sequence.split(' \n')]
    newSeq = []
    count = 0
    for i in sequence:
        newSeq = i.split()
    print(len(newSeq)/3)
    for i in range(0, len(newSeq)-8, 9):
        if int(newSeq[i]) + int(newSeq[i+3]) > int(newSeq[i+6]) and int(newSeq[i+6]) + int(newSeq[i+3]) > int(newSeq[i]) and int(newSeq[i]) + int(newSeq[i+6]) > int(newSeq[i+3]):
            count += 1
        if int(newSeq[i+1]) + int(newSeq[i+4]) > int(newSeq[i+7]) and int(newSeq[i+7]) + int(newSeq[i+4]) > int(newSeq[i+1]) and int(newSeq[i+1]) + int(newSeq[i+7]) > int(newSeq[i+4]):
            count += 1
        if int(newSeq[i+2]) + int(newSeq[i+5]) > int(newSeq[i+8]) and int(newSeq[i+8]) + int(newSeq[i+5]) > int(newSeq[i+2]) and int(newSeq[i+2]) + int(newSeq[i+8]) > int(newSeq[i+5]):
            count += 1
    return count

f = open('day3-adventOfCode.txt', 'r')
sequence = f.read()
print(triangleCount(sequence))
