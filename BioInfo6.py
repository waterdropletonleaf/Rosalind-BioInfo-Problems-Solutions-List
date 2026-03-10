import Bio.Data

def hamming_distance(S,T):
    if len(S) != len(T):
        return 1 
    else:
        count = 0
        for x in range(len(S)):
            if S[x] != T[x]:
                count = count + 1
    return count

strand1 = input("Strand1 ")
strand2 = input("Strand2 ")


print(hamming_distance(strand1, strand2))
