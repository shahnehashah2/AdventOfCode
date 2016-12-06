"""
Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.
Or are they?
The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.
In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.
In your puzzle input, how many of the listed triangles are possible?
"""

def triangleCount(sequence):
    sequence = sequence.split('\n')
    count = 0
    for i in sequence:
        i = i.split()
        i[0] = int(i[0])
        i[1] = int(i[1])
        i[2] = int(i[2])
        if (i[0] + i[1] > i[2]) and (i[2] + i[1] > i[0]) and (i[0] + i[2] > i[1]):
            count += 1
    return count

f = open('day3-adventOfCode.txt', 'r')
sequence = f.read()
print(triangleCount(sequence))
