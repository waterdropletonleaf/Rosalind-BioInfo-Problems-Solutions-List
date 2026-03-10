

def counter(s, t):
    long_string = s 
    short_string = t
    placement = []
    point1 = 0 
    point2 = len(t)
    for x in range(len(long_string)):
        try: 
            if short_string == long_string[point1:point2]:
                placement.insert(x)
                print(x)
                point1 = point1+1
                point2 = point2+1
            else:
                point1 = point1+1
                point2 = point2+1
            
        except:
            break
    
    return placement


print(counter("GATATATGCATATACTT" , "ATAT"))