# Counting Data Nucleotides

dna = input("give me a DNA string")
a = 0
c = 0
g = 0
t = 0
for x in dna:
    if x == "A":
        a = a + 1
    elif x == "C":
        c = c +1 
    elif x == "G":
        g = g + 1
    elif x == "T":
        t = t + 1 
print(a, c, g, t)