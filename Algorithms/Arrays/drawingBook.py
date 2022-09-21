import math

def pageCount(n, p):
    front_count = math.floor(p/2)
    if n%2 == 1:
        back_count = math.floor((n-p)/2)
    else:
        back_count = math.ceil((n-p)/2)
    
    if front_count <= back_count:
        return front_count
    else:
        return back_count

print(pageCount(5,3))