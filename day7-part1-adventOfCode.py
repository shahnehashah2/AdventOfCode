"""
While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).
An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.
For example:
abba[mnop]qrst supports TLS (abba outside square brackets).
abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
How many IPs in your puzzle input support TLS?
"""
from re import findall

def checkabba(j):
    if len(j) < 4:
        return False
    for k in range(len(j)-3):
        if j[k] == j[k+3] and j[k+1] == j[k+2] and j[k] != j[k+1]:
            return True
    return False

def checkTLS(sequence):
    sequence = sequence.split('\n')
    tls = 0
    for i in sequence:
        found = 0
        hypernetFound = 0
        item = findall(r'(\[?\w+\]?)', i)
        for j in item:
            if j[0] == '[':
                if checkabba(j[1:len(j)-1]):
                    hypernetFound = 1
                    continue
            if checkabba(j):
                found = 1
        if found and not hypernetFound:
            tls += 1
    return tls

f = open('day7-adventOfCode.txt', 'r')
sequence = f.read()
print(checkTLS(sequence))
