def isValidateSubsequesnce(arrayOne,arrayTwo):

    # seqIdx=0
    #
    # for value in arrayOne:
    #     if seqIdx == len(arrayTwo):
    #         break
    #     if arrayTwo[seqIdx] == value:
    #         seqIdx +=1
    #
    # return seqIdx  == len(arrayTwo)


    seqIdx=0
    arrayIdx=0

    while arrayIdx < len(arrayOne) and seqIdx < len(arrayTwo):

        if arrayOne[arrayIdx] == arrayTwo[seqIdx]:
            seqIdx +=1
        arrayIdx +=1

    return seqIdx  == len(arrayTwo)




    # for value in arrayTwo:
    #     if value not in arrayOne:
    #         return False
    # return True
    # pass

arrayOne=[1,2,3,4]
arrayTwo=[1,4]
k=isValidateSubsequesnce(arrayOne,arrayTwo)
print(k)