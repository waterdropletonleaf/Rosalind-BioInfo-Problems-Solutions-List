


# def fibo(mon, multi):
#     pair = 0
#     k = multi
#     for x in range(mon):
#         if x == 1 or x ==2: 
#             print("This ran")
#             return 1
#         else:
#             pair = fibo(x - 1, k) 
#             return type(pair)
            # pair = pair + fibo(x - 1, k) + k * fibo(x - 2 , k)
        # return pair
    
    
def fibo(mon, multi):
    k = multi
    if mon == 1 or mon == 2: 
        return 1
    else:
        return int(fibo(mon-1 , k)) + k * int(fibo(mon-2, k))
    
print(fibo(35,5))

