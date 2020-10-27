import re
def reversesentence(s):
    #convert a string to list

    s=re.findall(r"[\w']+|[.,!?;]", str(s))
    i=0
    j=len(s)-1
    while i<=j:
        # check if the character is punctuation and skip
        if not s[i].isalpha():
            i+=1
        if not s[j].isalpha():
            j-=1
        else:

            #swap the words
            s[i],s[j]=s[j],s[i]

            #check for capitalization
            if s[j][0].isupper():
                s[i]=s[i].capitalize()
                s[j]=s[j].lower()
            i+=1
            j-=1

    #convert back to string
    out=""
    for word in s:
        if not word.isalpha() or out is "":
            out += word
        else:
            out += " " + word
    return out


print("enter sentence")
s=str(input())
#print(reverese(s))
print(reversesentence(s))