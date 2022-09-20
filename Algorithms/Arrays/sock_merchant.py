match = False
num_of_pairs = 0

def sockMerchant(n, ar):
    # Write your code here
    
    if n < 2:
        return 0
    ar.sort()
    socks = ar
    global match
    global num_of_pairs
    num_of_pairs = 0
    for i in range(0,n-1):
        if match == True:
            match = False
        else:
            if socks[i] == socks[i+1]:
                match = True
                num_of_pairs += 1
    
    return num_of_pairs


print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))