def caesarCipher(s, k):
    arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cipher = ''
    
    for i in s:
        if i in arr:
            index = arr.index(i)
            cipher += arr[(index + k)%26]
        elif i.lower() in arr:
            index = arr.index(i.lower())
            cipher += arr[(index + k)%26].upper()
        else:
            cipher += i
    
    return cipher

print(caesarCipher('aBc-defghijkz',3))