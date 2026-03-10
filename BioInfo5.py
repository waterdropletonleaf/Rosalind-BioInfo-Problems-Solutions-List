greatest = 0
greatest_value = 0
count = 0
dna_strands= input("Sequence: ") + ">"
for x in range(len(dna_strands)):
    if dna_strands[x] == '>':
        test_val = dna_strands[x+ 1 : x + 14]
        start_val = x + 14
    elif (dna_strands[x] == 'C' or dna_strands[x] == 'G' or dna_strands[x] == 'A' or dna_strands[x] == 'T') and dna_strands[x + 1] == ">":
        end_val = x + 1
        new_string = dna_strands[start_val:end_val]
        count = 0
        for l in new_string:
            if l == "C" or l == "G":
                count = count + 1
        temp_result = count/len(new_string)
        if greatest_value < temp_result:
            greatest_value = temp_result
            greatest = test_val
            
print(greatest)
print(greatest_value)

result = f"{greatest_value:6%}"
print(result)
                

    
test_string = "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG" 
# print(test_string) 
# print(len(test_string))
    

# for x in dna_strand:
#     if x == "C" or x == "G":
#         count = count + 1
# result = f"{count/len(dna_strand):6%}"
# print(result)
# elif (dna_strands[x] == 'C' or dna_strands[x] == 'G' or dna_strands[x] == 'A' or dna_strands[x] == 'T') and (dna_strands[x + 1] == ">" or x + 1 > len(dna_strands)):
#         end_val = x + 1
#         new_string = dna_strands[start_val:end_val]