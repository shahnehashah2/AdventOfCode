from collections import Counter
from string import digits
import re

def alphabet_position(letter):
    """Get rotation value for the letter"""
    if letter.isalpha():
        return ord(letter.lower()) - 97
    else:
        print ('Invalid input for encryption key')
        exit()

def rotate_character(char, rot):
    """Encrypt each character by integer rot"""
    cipher = ''
    if ord(char) < 97:
        cipher = chr(((alphabet_position(char) + rot) % 26) + 65)
    else:
        cipher = chr(((alphabet_position(char) + rot) % 26) + 97)
    return cipher

def encrypt(mess, rot):
    """Use Caesar Encryption to encrypt the message"""
    cipherText = ''
    for c in mess:
        if c.isalpha():
            cipherText += rotate_character(c, rot)
        else:
            cipherText += c
    return cipherText

def checkDecoy(sequence):
    newSeq = []
    checksum = []
    index = 0
    f = open('day4-adventOfCodeOutput.txt', 'w')
    sequence = sequence.replace('-', ' ').split('\n')
    for i in sequence:
        checksum.append(''.join(x for x in i if x.isdigit()))
        i = ''.join(x for x in i if not x.isdigit())
        newSeq.append([x for x in re.split('\[(.*?)\]', i.strip())])
    for item in newSeq:
        f.write(str(item) + checksum[index] + encrypt(item[0], int(checksum[index])) + '\n')
        index += 1

f = open('day4-adventOfCode.txt', 'r')
sequence = f.read()
checkDecoy(sequence)
