def caesarCipherEncryptor(string, key):
    #temp={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
    newletters=[]
    k=0
    newkey=key%26
    alphab = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newlettercode=alphab.index(letter)+newkey
        if newlettercode <= 25:
            k=alphab[newlettercode]
        else:
            k=alphab[-1 + newlettercode%25]

        newletters.append(k)
    return "".join(newletters)



#     newletters=[]
#     newkey=key%26
#     for letter in string:
#         newletters.append(getnew(letter,newkey))
#     return "".join(newletters)
#
# def getnew(letter,newkey):
#     alphab = list("abcdefghijklmnopqrstuvwxyz")
#     newlettercode=alphab.index(letter)+key
#     return alphab[newlettercode] if newlettercode<=25 else alphab[-1 + newlettercode%25]
#     pass


print("caesarCipherEncryptor")
print("Enter a set of alphabets:")
string=input("")
print("Enter a number by which the letters should be shifted")
key=int(input())
print(caesarCipherEncryptor(string, key))