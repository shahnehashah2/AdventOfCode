"""
You would also like to know which IPs support SSL (super-secret listening).
An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.
For example:
aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
How many IPs in your puzzle input support SSL?
"""
from re import findall

def checkbab(pattern, k):
    for i in pattern:
        for j in i:
            if j and str(j[1]+j[0]+j[1]) in k:
                return 1
    return 0

def checkaba(j):
    if len(j) < 3:
        return False
    pattern = []
    for k in range(len(j)-2):
        if j[k] == j[k+2] and j[k] != j[k+1]:
            pattern.append(j[k:k+3])
    return pattern

def checkSSL(sequence):
    sequence = sequence.split('\n')
    ssl = 0
    #Make a list out the string dividing by supernet and hypernet
    for i in sequence:
        found = 0
        item = findall(r'(\[?\w+\]?)', i)
        hypernet = []
        supernet = []
        # Dividing the list into supernet and hypernet sublists
        for j in item:
            if j[0] == '[':
                hypernet.append(j)
            else:
                supernet.append(j)
        pattern = []
        for k in supernet:
            pattern.append(checkaba(k))
        for k in hypernet:
            found += checkbab(pattern, k)
        if found:
            ssl += 1
    return ssl

f = open('day7-adventOfCode.txt', 'r')
sequence = f.read()
print(checkSSL(sequence))
