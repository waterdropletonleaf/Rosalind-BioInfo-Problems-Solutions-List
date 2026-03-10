complement= ""

dna = input("Give me a DNA string ")

for x in dna:
    if x == "A":
        complement = complement + "T"
    elif x == "C":
        complement = complement + "G"
    elif x == "G":
        complement = complement + "C"
    elif x == "T":
        complement = complement + "A"

print("                                       ",complement[::-1])