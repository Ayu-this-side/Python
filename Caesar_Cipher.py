#Caesar Cipher
a = input("Type 'Encrypt' for encryption, type 'decrypt' for decryption: ")

b = input("Type your message: ").upper()

c =int(input("Type the shift number: "))

list1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
if a=='Encrypt':
    for i in b:
        if i in list1:
            d = (list1.index(i))
            e = (d + c)%26
            f = list1[e]
            g = f.lower()
            print(g,end="")
    
elif a=='decrypt':
    for j in b:
        if j in list1:
            h = (list1.index(j))
            l = (h - c)
            if l<0:
                l = l+26
                x = l%26
                m = list1[x]
                n = m.lower()
                print(n,end="")
            else:
                l = (h - c)%26
                m = list1[l]
                n = m.lower()
                print(n,end="")




                
